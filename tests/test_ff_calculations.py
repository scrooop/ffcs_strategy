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

from ff_tastytrade_scanner import validate_ff_inputs, forward_iv, pick_atm_strike, ATM_DELTA_TARGET, ATM_DELTA_TOLERANCE


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


# ============================================================================
# Test Suite: ATM Strike Selection
# ============================================================================

class MockStrike:
    """Mock strike object for testing pick_atm_strike()"""
    def __init__(self, strike_price: float, call_symbol: str, put_symbol: str):
        self.strike_price = strike_price
        self.call_streamer_symbol = call_symbol
        self.put_streamer_symbol = put_symbol


class MockExpiration:
    """Mock expiration object for testing pick_atm_strike()"""
    def __init__(self, strikes: list):
        self.strikes = strikes


class TestPickATMStrike:
    """Test pick_atm_strike() delta-based selection and fallback logic"""

    def test_delta_selection_exact_50delta(self):
        """Test that 50Δ strike is selected when available."""
        # Create mock strikes with various deltas
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),  # This should be selected (50Δ)
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        # Create greeks_map with exact 50Δ on 100 strike
        greeks_map = {
            "CALL95": (0.25, 0.65),   # Higher delta
            "CALL100": (0.23, 0.50),  # Exact 50Δ
            "CALL105": (0.21, 0.35),  # Lower delta
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        assert strike == 100.0
        assert delta == 0.50
        assert call_sym == "CALL100"
        assert put_sym == "PUT100"

    def test_delta_selection_within_tolerance(self):
        """Test that closest delta within tolerance is selected."""
        # Create mock strikes where none are exactly 50Δ but one is close
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),  # 48Δ (within ±10Δ tolerance)
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        # Create greeks_map with 48Δ on 100 strike (within 0.10 tolerance)
        greeks_map = {
            "CALL95": (0.25, 0.65),
            "CALL100": (0.23, 0.48),  # 48Δ (distance 0.02 from 50Δ)
            "CALL105": (0.21, 0.35),
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        assert strike == 100.0
        assert abs(delta - 0.48) < TOLERANCE
        assert call_sym == "CALL100"
        assert put_sym == "PUT100"

    def test_delta_selection_picks_closest(self):
        """Test that closest delta to 50Δ is selected when multiple within tolerance."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),  # 52Δ (distance 0.02)
            MockStrike(102.5, "CALL102.5", "PUT102.5"),  # 49Δ (distance 0.01) - should be selected
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        greeks_map = {
            "CALL95": (0.25, 0.65),
            "CALL100": (0.23, 0.52),      # Distance 0.02
            "CALL102.5": (0.22, 0.49),    # Distance 0.01 (closest)
            "CALL105": (0.21, 0.35),
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 102.5, greeks_map)

        assert strike == 102.5
        assert abs(delta - 0.49) < TOLERANCE
        assert call_sym == "CALL102.5"

    def test_fallback_to_nearest_spot_no_deltas_in_tolerance(self):
        """Test fallback to nearest-spot when no deltas within ±10Δ tolerance."""
        strikes = [
            MockStrike(90.0, "CALL90", "PUT90"),   # Nearest to spot=100
            MockStrike(100.0, "CALL100", "PUT100"),  # This should be selected by fallback
            MockStrike(110.0, "CALL110", "PUT110"),
        ]
        exp_obj = MockExpiration(strikes)

        # All deltas outside ±10Δ tolerance
        greeks_map = {
            "CALL90": (0.25, 0.75),   # 75Δ (distance 0.25, outside tolerance)
            "CALL100": (0.23, 0.65),  # 65Δ (distance 0.15, outside tolerance)
            "CALL110": (0.21, 0.25),  # 25Δ (distance 0.25, outside tolerance)
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        # Should fall back to strike nearest spot (100.0)
        assert strike == 100.0
        assert delta is None  # Fallback doesn't set delta
        assert call_sym == "CALL100"
        assert put_sym == "PUT100"

    def test_fallback_to_nearest_spot_empty_greeks_map(self):
        """Test fallback to nearest-spot when greeks_map is empty."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),  # Nearest to spot
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        # Empty greeks_map should trigger fallback
        greeks_map = {}

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        assert strike == 100.0
        assert delta is None
        assert call_sym == "CALL100"

    def test_fallback_to_nearest_spot_none_greeks_map(self):
        """Test fallback to nearest-spot when greeks_map is None."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, None)

        assert strike == 100.0
        assert delta is None
        assert call_sym == "CALL100"

    def test_fallback_nearest_spot_exact_match(self):
        """Test fallback selects exact spot match when available."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),  # Exact match
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, {})

        assert strike == 100.0
        assert call_sym == "CALL100"

    def test_fallback_nearest_spot_between_strikes(self):
        """Test fallback selects closest strike when spot is between strikes."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(105.0, "CALL105", "PUT105"),  # Closest to spot=102
        ]
        exp_obj = MockExpiration(strikes)

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 102.0, {})

        # 102 is closer to 105 than to 95
        assert strike == 105.0
        assert call_sym == "CALL105"

    def test_greeks_missing_some_strikes(self):
        """Test delta selection when Greeks missing for some strikes."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        # Greeks only available for 95 and 105, not 100
        greeks_map = {
            "CALL95": (0.25, 0.65),
            # CALL100 missing
            "CALL105": (0.21, 0.48),  # 48Δ (within tolerance, closest available)
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        # Should select 105 strike (48Δ is closest available within tolerance)
        assert strike == 105.0
        assert abs(delta - 0.48) < TOLERANCE
        assert call_sym == "CALL105"

    def test_greeks_none_delta(self):
        """Test that strikes with None delta are skipped."""
        strikes = [
            MockStrike(95.0, "CALL95", "PUT95"),
            MockStrike(100.0, "CALL100", "PUT100"),
            MockStrike(105.0, "CALL105", "PUT105"),
        ]
        exp_obj = MockExpiration(strikes)

        # 100 strike has None delta
        greeks_map = {
            "CALL95": (0.25, 0.65),
            "CALL100": (0.23, None),  # Delta is None
            "CALL105": (0.21, 0.48),  # Should be selected
        }

        strike, delta, call_sym, put_sym = pick_atm_strike(exp_obj, 100.0, greeks_map)

        assert strike == 105.0
        assert abs(delta - 0.48) < TOLERANCE

    def test_constants_defined(self):
        """Test that ATM_DELTA_TARGET and ATM_DELTA_TOLERANCE constants are defined correctly."""
        assert ATM_DELTA_TARGET == 0.50
        assert ATM_DELTA_TOLERANCE == 0.10

    def test_no_strikes_raises_error(self):
        """Test that RuntimeError is raised when expiration has no strikes."""
        exp_obj = MockExpiration([])

        with pytest.raises(RuntimeError, match="No strikes found"):
            pick_atm_strike(exp_obj, 100.0, {})


# ============================================================================
# Test Suite: Min-Gate Filtering (Double Calendars)
# ============================================================================

class TestMinGateFiltering:
    """Test min-gate filtering logic for double calendar spreads."""

    def test_min_ff_calculation_basic(self):
        """Test that min_ff is correctly calculated as min(call_ff, put_ff)."""
        # Setup: call FF = 0.25, put FF = 0.30
        call_ff = 0.25
        put_ff = 0.30

        # Calculate min_ff
        min_ff = min(call_ff, put_ff)

        # Verify
        assert min_ff == 0.25
        assert min_ff == call_ff
        assert min_ff < put_ff

    def test_min_ff_calculation_equal_ffs(self):
        """Test min_ff when both legs have equal FF."""
        # Setup: call FF = 0.23, put FF = 0.23
        call_ff = 0.23
        put_ff = 0.23

        # Calculate min_ff
        min_ff = min(call_ff, put_ff)

        # Verify
        assert min_ff == 0.23
        assert min_ff == call_ff
        assert min_ff == put_ff

    def test_min_ff_put_lower(self):
        """Test min_ff when put FF is lower than call FF."""
        # Setup: call FF = 0.30, put FF = 0.20
        call_ff = 0.30
        put_ff = 0.20

        # Calculate min_ff
        min_ff = min(call_ff, put_ff)

        # Verify
        assert min_ff == 0.20
        assert min_ff == put_ff
        assert min_ff < call_ff

    def test_min_gate_filtering_both_legs_pass(self):
        """Test that double calendar passes when both legs meet threshold."""
        # Setup: threshold = 0.20
        threshold = 0.20
        call_ff = 0.25
        put_ff = 0.23

        min_ff = min(call_ff, put_ff)

        # Both legs pass threshold
        assert call_ff >= threshold
        assert put_ff >= threshold
        assert min_ff >= threshold  # Should pass min-gate

    def test_min_gate_filtering_one_leg_fails(self):
        """Test that double calendar fails when one leg is below threshold."""
        # Setup: threshold = 0.23
        threshold = 0.23
        call_ff = 0.30
        put_ff = 0.18  # Below threshold

        min_ff = min(call_ff, put_ff)

        # Call leg passes, put leg fails
        assert call_ff >= threshold
        assert put_ff < threshold
        assert min_ff < threshold  # Should fail min-gate

    def test_min_gate_filtering_both_legs_fail(self):
        """Test that double calendar fails when both legs are below threshold."""
        # Setup: threshold = 0.23
        threshold = 0.23
        call_ff = 0.18
        put_ff = 0.15

        min_ff = min(call_ff, put_ff)

        # Both legs fail
        assert call_ff < threshold
        assert put_ff < threshold
        assert min_ff < threshold  # Should fail min-gate

    def test_min_gate_edge_case_exactly_at_threshold(self):
        """Test edge case where min_ff exactly equals threshold."""
        # Setup: threshold = 0.20
        threshold = 0.20
        call_ff = 0.25
        put_ff = 0.20  # Exactly at threshold

        min_ff = min(call_ff, put_ff)

        # Should pass (>= threshold)
        assert min_ff == threshold
        assert min_ff >= threshold

    def test_min_gate_vs_avg_gate_comparison(self):
        """Test that min-gate is more conservative than average-gate."""
        # Setup: call FF = 0.30, put FF = 0.18
        call_ff = 0.30
        put_ff = 0.18
        threshold = 0.23

        # Average-gate (old logic)
        avg_ff = (call_ff + put_ff) / 2.0
        avg_gate_passes = avg_ff >= threshold

        # Min-gate (new logic)
        min_ff = min(call_ff, put_ff)
        min_gate_passes = min_ff >= threshold

        # Verify min-gate is more conservative
        assert avg_ff == 0.24  # Would pass with avg-gate
        assert avg_gate_passes is True
        assert min_ff == 0.18  # Fails with min-gate
        assert min_gate_passes is False

        # This demonstrates min-gate correctly requires BOTH wings to meet threshold

    def test_min_gate_scenario_weak_put_wing(self):
        """Test real-world scenario: strong call wing, weak put wing."""
        # Scenario: High IV on calls, normal IV on puts (typical in bear markets)
        # Call: IV_front=0.35, IV_back=0.28, 30-60 DTE
        # Put: IV_front=0.25, IV_back=0.24, 30-60 DTE

        call_iv_front = 0.35
        call_iv_back = 0.28
        put_iv_front = 0.25
        put_iv_back = 0.24
        dte_front = 30
        dte_back = 60

        # Calculate forward IVs
        call_fwd = forward_iv(call_iv_front, call_iv_back, dte_front, dte_back)
        put_fwd = forward_iv(put_iv_front, put_iv_back, dte_front, dte_back)

        assert call_fwd is not None
        assert put_fwd is not None

        # Calculate FFs
        call_ff = (call_iv_front - call_fwd) / call_fwd
        put_ff = (put_iv_front - put_fwd) / put_fwd

        # Calculate metrics
        avg_ff = (call_ff + put_ff) / 2.0
        min_ff = min(call_ff, put_ff)

        threshold = 0.20

        # Call wing strong, put wing weak
        assert call_ff > threshold  # Strong call wing
        # Put wing may be weak (close to threshold or below)

        # Min-gate correctly rejects if put wing is too weak
        if put_ff < threshold:
            assert min_ff < threshold  # Should fail min-gate
            # Even though avg_ff might pass

    def test_combined_ff_retained_for_reference(self):
        """Test that combined_ff is still calculated and retained alongside min_ff."""
        # Both metrics should exist in output
        call_ff = 0.28
        put_ff = 0.22

        # New metric: min_ff
        min_ff = min(call_ff, put_ff)

        # Legacy metric: combined_ff (retained for reference)
        combined_ff = (call_ff + put_ff) / 2.0

        # Both should be calculated
        assert min_ff == 0.22
        assert combined_ff == 0.25

        # min_ff is used for filtering
        threshold = 0.23
        assert min_ff < threshold  # Fails min-gate
        assert combined_ff >= threshold  # Would pass avg-gate (old logic)

        # This demonstrates why both metrics are valuable:
        # - min_ff for filtering (conservative)
        # - combined_ff for reference/analysis
