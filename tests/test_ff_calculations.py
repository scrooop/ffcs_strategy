#!/usr/bin/env python3
"""
Unit tests for Forward Factor (FF) calculation formulas.

Tests the complete FF calculation pipeline:
1. validate_ff_inputs() - Input validation and edge case detection
2. forward_iv() - Forward implied volatility calculation
3. FF formula - Forward Factor: FF = (IV_front - IV_fwd) / IV_fwd

Reference formulas:
- Forward variance: V_fwd = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)
- Forward IV: IV_fwd = sqrt(V_fwd)
- Forward Factor: FF = (IV_front - IV_fwd) / IV_fwd

All tests use 1e-8 tolerance for floating-point comparisons.
"""

import pytest
import math
import sys
from pathlib import Path

# Add scripts directory to path to import scanner functions
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from ff_tastytrade_scanner import validate_ff_inputs, forward_iv


# ============================================================================
# Test Constants
# ============================================================================

TOLERANCE = 1e-8  # Float comparison tolerance


# ============================================================================
# Test Helpers
# ============================================================================

def calculate_forward_variance(iv_front: float, iv_back: float, dte_front: int, dte_back: int) -> float:
    """
    Calculate forward variance using the variance decomposition formula.

    V_fwd = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)
    where T = DTE/365

    Returns:
        Forward variance (not IV, but variance)
    """
    T1 = dte_front / 365.0
    T2 = dte_back / 365.0

    numerator = (iv_back ** 2) * T2 - (iv_front ** 2) * T1
    denominator = T2 - T1

    return numerator / denominator


def calculate_forward_factor(iv_front: float, iv_fwd: float) -> float:
    """
    Calculate Forward Factor.

    FF = (IV_front - IV_fwd) / IV_fwd

    Returns:
        Forward Factor (decimal)
    """
    return (iv_front - iv_fwd) / iv_fwd


# ============================================================================
# Test Suite: Forward Variance Formula
# ============================================================================

class TestForwardVarianceFormula:
    """Test forward variance calculation: V_fwd = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)"""

    def test_basic_forward_variance(self):
        """Test forward variance with known values."""
        # Setup: 30% IV front, 25% IV back, 30-60 DTE
        iv_front = 0.30
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Calculate expected forward variance
        T1 = 30 / 365.0
        T2 = 60 / 365.0

        expected_variance = ((0.25 ** 2) * T2 - (0.30 ** 2) * T1) / (T2 - T1)

        # Calculate actual using helper
        actual_variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)

        # Verify
        assert abs(actual_variance - expected_variance) < TOLERANCE

    def test_nonpositive_forward_variance_exact_zero(self):
        """Test edge case where forward variance is exactly zero."""
        # Setup: IV_back^2 * T2 == IV_front^2 * T1
        # This means both expirations have same total variance

        # Choose values where variance is equal
        # If IV_front = 0.30, DTE_front = 30, then variance = 0.09 * (30/365)
        # We need IV_back^2 * (60/365) = 0.09 * (30/365)
        # IV_back^2 = 0.09 * (30/60) = 0.045
        # IV_back = sqrt(0.045) ≈ 0.2121

        iv_front = 0.30
        dte_front = 30
        dte_back = 60
        iv_back = math.sqrt(0.09 * (30.0 / 60.0))  # Should give exactly zero variance

        variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)

        # Variance should be zero (or very close)
        assert abs(variance) < TOLERANCE

        # Validation should detect this
        skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
        assert skip_reason is not None
        assert "Non-positive forward variance" in skip_reason

    def test_nonpositive_forward_variance_negative(self):
        """Test edge case where forward variance is negative."""
        # Setup: IV_back^2 * T2 < IV_front^2 * T1
        # This happens when front IV is "too hot" relative to back IV

        iv_front = 0.50  # Very high front IV
        iv_back = 0.25   # Lower back IV
        dte_front = 30
        dte_back = 60

        # Verify this creates negative variance
        variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)
        assert variance < 0

        # Validation should detect this
        skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
        assert skip_reason is not None
        assert "Non-positive forward variance" in skip_reason

    def test_forward_variance_positive_cases(self):
        """Test that normal market conditions produce positive variance."""
        test_cases = [
            # (iv_front, iv_back, dte_front, dte_back)
            (0.20, 0.22, 30, 60),   # Normal backwardation
            (0.30, 0.25, 30, 60),   # Moderate backwardation
            (0.15, 0.20, 60, 90),   # Contango
            (0.25, 0.25, 30, 90),   # Flat term structure (longer window)
        ]

        for iv_front, iv_back, dte_front, dte_back in test_cases:
            variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)

            # Should be positive
            assert variance > 0, f"Expected positive variance for {iv_front}, {iv_back}, {dte_front}, {dte_back}"

            # Validation should pass
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            assert skip_reason is None, f"Expected valid inputs for {iv_front}, {iv_back}, {dte_front}, {dte_back}"


# ============================================================================
# Test Suite: Forward IV Calculation
# ============================================================================

class TestForwardIV:
    """Test forward IV: IV_fwd = sqrt(V_fwd)"""

    def test_forward_iv_basic(self):
        """Test forward IV calculation with known values."""
        # Setup
        iv_front = 0.30
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Calculate forward IV
        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)

        # Verify it's not None
        assert fwd_iv is not None

        # Calculate expected value manually
        variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)
        expected_fwd_iv = math.sqrt(variance)

        # Verify
        assert abs(fwd_iv - expected_fwd_iv) < TOLERANCE

    def test_forward_iv_returns_none_for_invalid_inputs(self):
        """Test that forward_iv returns None for invalid inputs."""
        test_cases = [
            # (iv_front, iv_back, dte_front, dte_back, description)
            (0.50, 0.25, 30, 60, "Non-positive variance"),
            (-0.25, 0.25, 30, 60, "Negative IV_front"),
            (0.25, -0.25, 30, 60, "Negative IV_back"),
            (0.25, 0.25, 60, 30, "Back DTE < Front DTE"),
            (0.25, 0.25, 30, 30, "Equal DTEs"),
        ]

        for iv_front, iv_back, dte_front, dte_back, description in test_cases:
            fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
            assert fwd_iv is None, f"Expected None for {description}"

    def test_forward_iv_reference_values(self):
        """Test forward IV against reference calculations."""
        # Reference case 1: 30-60 DTE, moderate backwardation
        # Calculation:
        # T1 = 30/365 = 0.0822, T2 = 60/365 = 0.1644
        # numerator = (0.25^2 * 0.1644) - (0.30^2 * 0.0822) = 0.010275 - 0.007398 = 0.002877
        # denominator = 0.1644 - 0.0822 = 0.0822
        # variance = 0.002877 / 0.0822 = 0.035
        # fwd_iv = sqrt(0.035) = 0.1871
        fwd_iv = forward_iv(0.30, 0.25, 30, 60)
        assert fwd_iv is not None
        assert abs(fwd_iv - 0.1871) < 0.001

        # Reference case 2: 60-90 DTE, slight backwardation
        fwd_iv = forward_iv(0.22, 0.20, 60, 90)
        assert fwd_iv is not None
        # Should be less than both IVs since it's the "forward" slice in contango
        assert fwd_iv < 0.22
        assert fwd_iv < 0.20

    def test_forward_iv_precision(self):
        """Test that forward IV maintains double-precision accuracy."""
        # Use values that might expose precision issues
        iv_front = 0.123456789012345
        iv_back = 0.234567890123456
        dte_front = 37
        dte_back = 73

        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
        assert fwd_iv is not None

        # Calculate expected value with full precision
        variance = calculate_forward_variance(iv_front, iv_back, dte_front, dte_back)
        expected = math.sqrt(variance)

        # Should match to within 1e-8
        assert abs(fwd_iv - expected) < TOLERANCE


# ============================================================================
# Test Suite: Forward Factor (FF) Formula
# ============================================================================

class TestForwardFactor:
    """Test FF: FF = (IV_front - IV_fwd) / IV_fwd"""

    def test_ff_formula_basic(self):
        """Test FF calculation with known values."""
        # Setup
        iv_front = 0.30
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Calculate forward IV
        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
        assert fwd_iv is not None

        # Calculate FF
        ff = calculate_forward_factor(iv_front, fwd_iv)

        # Verify FF is positive (backwardation case)
        assert ff > 0

        # Verify against manual calculation
        expected_ff = (iv_front - fwd_iv) / fwd_iv
        assert abs(ff - expected_ff) < TOLERANCE

    def test_ff_monotonicity_increasing_front_iv(self):
        """Test that FF increases as IV_front increases (holding other vars constant)."""
        # Setup: Fix back IV and DTEs, vary front IV
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Test increasing front IVs (all should produce valid forward variance)
        front_ivs = [0.20, 0.25, 0.28, 0.29]

        ffs = []
        for iv_front in front_ivs:
            # Skip if this would create non-positive variance
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            if skip_reason is not None:
                continue

            fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
            if fwd_iv is not None:
                ff = calculate_forward_factor(iv_front, fwd_iv)
                ffs.append(ff)

        # FF should be strictly increasing
        for i in range(len(ffs) - 1):
            assert ffs[i] < ffs[i+1], f"FF should increase: {ffs}"

    def test_ff_monotonicity_decreasing_back_iv(self):
        """Test that FF increases as IV_back decreases (holding other vars constant)."""
        # Setup: Fix front IV and DTEs, vary back IV
        iv_front = 0.30
        dte_front = 30
        dte_back = 60

        # Test decreasing back IVs (from high to low)
        # All should produce valid forward variance since front is higher
        back_ivs = [0.35, 0.32, 0.28, 0.26]

        ffs = []
        for iv_back in back_ivs:
            # Skip if this would create non-positive variance
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            if skip_reason is not None:
                continue

            fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
            if fwd_iv is not None:
                ff = calculate_forward_factor(iv_front, fwd_iv)
                ffs.append(ff)

        # FF should be strictly increasing (as back IV decreases)
        for i in range(len(ffs) - 1):
            assert ffs[i] < ffs[i+1], f"FF should increase as back IV decreases: {ffs}"

    def test_ff_reference_values(self):
        """Test FF against reference calculations from strategy documentation."""
        # Reference case: From CLAUDE.md example
        # "If your forward factor reads at 0.20 or higher"

        # Create a scenario that should produce FF ≥ 0.20
        iv_front = 0.30
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
        assert fwd_iv is not None

        ff = calculate_forward_factor(iv_front, fwd_iv)

        # This should produce a positive FF (backwardation)
        assert ff > 0

        # Based on the calculation: fwd_iv ≈ 0.1871
        # FF = (0.30 - 0.1871) / 0.1871 ≈ 0.604
        assert abs(ff - 0.604) < 0.01

    def test_ff_sign_cases(self):
        """Test FF sign in different market conditions."""
        test_cases = [
            # (iv_front, iv_back, dte_front, dte_back, expected_sign, description)
            (0.30, 0.25, 30, 60, 1, "Backwardation: FF > 0"),
            (0.20, 0.25, 30, 60, -1, "Contango: FF < 0"),
        ]

        for iv_front, iv_back, dte_front, dte_back, expected_sign, description in test_cases:
            # Skip if invalid
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            if skip_reason is not None:
                continue

            fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
            if fwd_iv is not None:
                ff = calculate_forward_factor(iv_front, fwd_iv)

                if expected_sign > 0:
                    assert ff > 0, f"{description}: Expected FF > 0, got {ff}"
                else:
                    assert ff < 0, f"{description}: Expected FF < 0, got {ff}"


# ============================================================================
# Test Suite: Validation Function
# ============================================================================

class TestValidationFunction:
    """Test validate_ff_inputs() function"""

    def test_valid_inputs(self):
        """Test that valid inputs pass validation."""
        test_cases = [
            (0.30, 0.25, 30, 60),
            (0.20, 0.22, 30, 60),
            (0.15, 0.20, 60, 90),
            (0.25, 0.25, 30, 90),
        ]

        for iv_front, iv_back, dte_front, dte_back in test_cases:
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            assert skip_reason is None, f"Expected None for valid inputs: {iv_front}, {iv_back}, {dte_front}, {dte_back}"

    def test_negative_iv_front(self):
        """Test detection of negative IV_front."""
        skip_reason = validate_ff_inputs(-0.25, 0.25, 30, 60)
        assert skip_reason is not None
        assert "IV_front" in skip_reason

    def test_negative_iv_back(self):
        """Test detection of negative IV_back."""
        skip_reason = validate_ff_inputs(0.25, -0.25, 30, 60)
        assert skip_reason is not None
        assert "IV_back" in skip_reason

    def test_zero_iv_front(self):
        """Test detection of zero IV_front."""
        skip_reason = validate_ff_inputs(0.0, 0.25, 30, 60)
        assert skip_reason is not None
        assert "IV_front" in skip_reason

    def test_zero_iv_back(self):
        """Test detection of zero IV_back."""
        skip_reason = validate_ff_inputs(0.25, 0.0, 30, 60)
        assert skip_reason is not None
        assert "IV_back" in skip_reason

    def test_nan_iv(self):
        """Test detection of NaN IVs."""
        skip_reason = validate_ff_inputs(float('nan'), 0.25, 30, 60)
        assert skip_reason is not None
        assert "NaN or infinity" in skip_reason

        skip_reason = validate_ff_inputs(0.25, float('nan'), 30, 60)
        assert skip_reason is not None
        assert "NaN or infinity" in skip_reason

    def test_infinity_iv(self):
        """Test detection of infinity IVs."""
        skip_reason = validate_ff_inputs(float('inf'), 0.25, 30, 60)
        assert skip_reason is not None
        assert "NaN or infinity" in skip_reason

        skip_reason = validate_ff_inputs(0.25, float('inf'), 30, 60)
        assert skip_reason is not None
        assert "NaN or infinity" in skip_reason

    def test_zero_dte_front(self):
        """Test detection of zero DTE_front."""
        skip_reason = validate_ff_inputs(0.25, 0.25, 0, 60)
        assert skip_reason is not None
        assert "DTE_front" in skip_reason

    def test_zero_dte_back(self):
        """Test detection of zero DTE_back."""
        skip_reason = validate_ff_inputs(0.25, 0.25, 30, 0)
        assert skip_reason is not None
        assert "DTE_back" in skip_reason

    def test_negative_dte_front(self):
        """Test detection of negative DTE_front."""
        skip_reason = validate_ff_inputs(0.25, 0.25, -30, 60)
        assert skip_reason is not None
        assert "DTE_front" in skip_reason

    def test_negative_dte_back(self):
        """Test detection of negative DTE_back."""
        skip_reason = validate_ff_inputs(0.25, 0.25, 30, -60)
        assert skip_reason is not None
        assert "DTE_back" in skip_reason

    def test_back_dte_less_than_front(self):
        """Test detection of back DTE < front DTE."""
        skip_reason = validate_ff_inputs(0.25, 0.25, 60, 30)
        assert skip_reason is not None
        assert "back DTE must be > front DTE" in skip_reason

    def test_back_dte_equal_to_front(self):
        """Test detection of back DTE == front DTE."""
        skip_reason = validate_ff_inputs(0.25, 0.25, 30, 30)
        assert skip_reason is not None
        assert "back DTE must be > front DTE" in skip_reason

    def test_nonpositive_forward_variance(self):
        """Test detection of non-positive forward variance."""
        # Case 1: Negative variance (front IV too hot)
        skip_reason = validate_ff_inputs(0.50, 0.25, 30, 60)
        assert skip_reason is not None
        assert "Non-positive forward variance" in skip_reason

        # Case 2: Zero variance (exactly equal total variance)
        iv_front = 0.30
        dte_front = 30
        dte_back = 60
        iv_back = math.sqrt(0.09 * (30.0 / 60.0))

        skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
        assert skip_reason is not None
        assert "Non-positive forward variance" in skip_reason


# ============================================================================
# Test Suite: Integration Tests
# ============================================================================

class TestIntegration:
    """Integration tests for the complete FF calculation pipeline."""

    def test_complete_pipeline_valid_case(self):
        """Test complete pipeline from validation to FF calculation."""
        iv_front = 0.30
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Step 1: Validate inputs
        skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
        assert skip_reason is None

        # Step 2: Calculate forward IV
        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
        assert fwd_iv is not None
        assert fwd_iv > 0

        # Step 3: Calculate FF
        ff = calculate_forward_factor(iv_front, fwd_iv)
        assert ff > 0  # Backwardation case

        # Verify FF is in reasonable range for trading
        assert ff > 0.20, "This setup should meet minimum FF threshold"

    def test_complete_pipeline_invalid_case(self):
        """Test complete pipeline correctly handles invalid inputs."""
        iv_front = 0.50  # Too hot
        iv_back = 0.25
        dte_front = 30
        dte_back = 60

        # Step 1: Validate inputs (should fail)
        skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
        assert skip_reason is not None

        # Step 2: forward_iv should also return None
        fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
        assert fwd_iv is None

    def test_edge_case_coverage(self):
        """Test that validation catches all edge cases that forward_iv would reject."""
        # Cases where both validation AND forward_iv should reject
        edge_cases_both_reject = [
            # (iv_front, iv_back, dte_front, dte_back, description)
            (-0.25, 0.25, 30, 60, "Negative IV_front"),
            (0.25, -0.25, 30, 60, "Negative IV_back"),
            (0.25, 0.25, 60, 30, "Back < Front DTE"),
            (0.50, 0.25, 30, 60, "Non-positive variance"),
        ]

        for iv_front, iv_back, dte_front, dte_back, description in edge_cases_both_reject:
            # Validation should catch all these
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            assert skip_reason is not None, f"Validation should catch: {description}"

            # forward_iv should also return None
            fwd_iv = forward_iv(iv_front, iv_back, dte_front, dte_back)
            assert fwd_iv is None, f"forward_iv should return None for: {description}"

        # Cases where validation rejects but forward_iv might not
        # (validation is more strict and that's intentional)
        edge_cases_validation_only = [
            # (iv_front, iv_back, dte_front, dte_back, description)
            (0.25, 0.25, 0, 60, "Zero DTE_front"),
            (0.25, 0.25, 30, 0, "Zero DTE_back"),
            (float('nan'), 0.25, 30, 60, "NaN IV"),
            (0.25, float('inf'), 30, 60, "Inf IV"),
        ]

        for iv_front, iv_back, dte_front, dte_back, description in edge_cases_validation_only:
            # Validation should catch all these
            skip_reason = validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)
            assert skip_reason is not None, f"Validation should catch: {description}"
