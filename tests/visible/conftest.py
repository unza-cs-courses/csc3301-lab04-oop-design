"""
Pytest fixtures for Lab 4: OOP Design and Polymorphism
CSC3301 Programming Language Paradigms

Loads variant configuration and provides fixtures with sensible defaults.
"""
import json
import math
from pathlib import Path
from typing import Any

import pytest


# Default values used when no variant config exists (for template testing)
DEFAULT_VARIANT = {
    "student_id": "default_student",
    "lab": "lab04-oop-design",
    "shape_tests": {
        "circle": {
            "radius": 5.0,
            "expected_area": 78.5398,
            "expected_perimeter": 31.4159,
        },
        "rectangle": {
            "width": 4.0,
            "height": 3.0,
            "expected_area": 12.0,
            "expected_perimeter": 14.0,
        },
        "square": {
            "side": 5.0,
            "expected_area": 25.0,
            "expected_perimeter": 20.0,
        },
        "triangle": {
            "side_a": 3.0,
            "side_b": 4.0,
            "side_c": 5.0,
            "expected_area": 6.0,
            "expected_perimeter": 12.0,
        },
    },
    "payment_tests": {
        "amounts": [50.0, 100.0, 250.0],
        "credit_card_fee_percent": 3.0,
        "paypal_fee_percent": 2.9,
        "crypto_discount_percent": 2.0,
        "expected_credit_card": [51.5, 103.0, 257.5],
        "expected_paypal": [51.45, 102.9, 257.25],
        "expected_crypto": [49.0, 98.0, 245.0],
    },
    "observer_tests": {
        "event_types": ["user_login", "data_update", "notification", "error"],
        "emit_counts": [2, 3, 1],
        "test_payloads": [
            {"id": 123, "message": "test_default"},
            {"value": 42.5, "active": True},
        ],
    },
    "composition_tests": {
        "vehicle_types": ["Car", "Boat", "Plane"],
        "features": ["Engine", "Wheels", "Wings", "Propeller"],
        "test_combinations": [
            {"vehicle": "Car", "features": ["Engine", "Wheels"]},
            {"vehicle": "Boat", "features": ["Engine", "Propeller"]},
            {"vehicle": "Plane", "features": ["Engine", "Wings"]},
        ],
    },
}


def load_variant_config() -> dict[str, Any]:
    """
    Load variant configuration from .variant_config.json.

    Returns default values if config file doesn't exist,
    allowing tests to run on the template repository.
    """
    # Look for config in repo root (parent of tests directory)
    repo_root = Path(__file__).parent.parent.parent
    config_path = repo_root / ".variant_config.json"

    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)
        print(f"Loaded variant config for student: {config.get('student_id', 'unknown')}")
        return config

    print("No variant config found, using default values")
    return DEFAULT_VARIANT


# Load config once at module level
_variant_config = load_variant_config()


@pytest.fixture
def variant_config() -> dict[str, Any]:
    """Provide the complete variant configuration."""
    return _variant_config


@pytest.fixture
def student_id() -> str:
    """Provide the student ID."""
    return _variant_config["student_id"]


# Shape fixtures
@pytest.fixture
def circle_params() -> dict[str, float]:
    """Provide circle test parameters."""
    return _variant_config["shape_tests"]["circle"]


@pytest.fixture
def rectangle_params() -> dict[str, float]:
    """Provide rectangle test parameters."""
    return _variant_config["shape_tests"]["rectangle"]


@pytest.fixture
def square_params() -> dict[str, float]:
    """Provide square test parameters."""
    return _variant_config["shape_tests"]["square"]


@pytest.fixture
def triangle_params() -> dict[str, float]:
    """Provide triangle test parameters."""
    return _variant_config["shape_tests"]["triangle"]


@pytest.fixture
def all_shape_params() -> dict[str, dict]:
    """Provide all shape test parameters."""
    return _variant_config["shape_tests"]


# Payment fixtures
@pytest.fixture
def payment_amounts() -> list[float]:
    """Provide payment test amounts."""
    return _variant_config["payment_tests"]["amounts"]


@pytest.fixture
def payment_fees() -> dict[str, float]:
    """Provide payment fee percentages."""
    return {
        "credit_card": _variant_config["payment_tests"]["credit_card_fee_percent"],
        "paypal": _variant_config["payment_tests"]["paypal_fee_percent"],
        "crypto_discount": _variant_config["payment_tests"]["crypto_discount_percent"],
    }


@pytest.fixture
def expected_payments() -> dict[str, list[float]]:
    """Provide expected payment totals after fees/discounts."""
    return {
        "credit_card": _variant_config["payment_tests"]["expected_credit_card"],
        "paypal": _variant_config["payment_tests"]["expected_paypal"],
        "crypto": _variant_config["payment_tests"]["expected_crypto"],
    }


@pytest.fixture
def payment_tests() -> dict[str, Any]:
    """Provide all payment test parameters."""
    return _variant_config["payment_tests"]


# Observer pattern fixtures
@pytest.fixture
def event_types() -> list[str]:
    """Provide event types for observer pattern tests."""
    return _variant_config["observer_tests"]["event_types"]


@pytest.fixture
def emit_counts() -> list[int]:
    """Provide emit count values for testing."""
    return _variant_config["observer_tests"]["emit_counts"]


@pytest.fixture
def test_payloads() -> list[dict]:
    """Provide test payloads for event emission."""
    return _variant_config["observer_tests"]["test_payloads"]


@pytest.fixture
def observer_tests() -> dict[str, Any]:
    """Provide all observer pattern test parameters."""
    return _variant_config["observer_tests"]


# Composition fixtures
@pytest.fixture
def composition_tests() -> dict[str, Any]:
    """Provide composition pattern test parameters."""
    return _variant_config["composition_tests"]


@pytest.fixture
def vehicle_types() -> list[str]:
    """Provide vehicle types for composition tests."""
    return _variant_config["composition_tests"]["vehicle_types"]


@pytest.fixture
def vehicle_features() -> list[str]:
    """Provide features for composition tests."""
    return _variant_config["composition_tests"]["features"]


# Utility fixtures
@pytest.fixture
def tolerance() -> float:
    """Provide floating-point comparison tolerance."""
    return 0.01


@pytest.fixture
def assert_float_equal(tolerance):
    """Provide a helper function to compare floats with tolerance."""
    def _assert_float_equal(actual: float, expected: float, msg: str = ""):
        assert abs(actual - expected) < tolerance, (
            f"{msg}: expected {expected}, got {actual} (tolerance: {tolerance})"
        )
    return _assert_float_equal
