#!/usr/bin/env python3
"""
Variant Generator for Lab 4: OOP Design and Polymorphism
CSC3301 Programming Language Paradigms

Generates deterministic, student-specific test values based on student ID hash.
"""
import hashlib
import json
import sys
from pathlib import Path


def generate_variant(student_id: str) -> dict:
    """
    Generate a deterministic variant configuration based on student ID.

    The variant includes:
    - Shape dimensions for testing (circles, rectangles, triangles, squares)
    - Payment amounts for strategy pattern tests
    - Event types for observer pattern tests

    Args:
        student_id: Unique student identifier (username or ID number)

    Returns:
        Dictionary containing all variant-specific test values
    """
    # Create deterministic hash from student ID
    hash_bytes = hashlib.sha256(student_id.encode()).digest()

    # Use different portions of the hash for different values
    def get_value(index: int, min_val: int, max_val: int) -> int:
        """Extract a deterministic value from hash bytes."""
        byte_val = hash_bytes[index % len(hash_bytes)]
        return min_val + (byte_val % (max_val - min_val + 1))

    def get_float(index: int, min_val: float, max_val: float, decimals: int = 2) -> float:
        """Extract a deterministic float from hash bytes."""
        byte_val = hash_bytes[index % len(hash_bytes)]
        raw = min_val + (byte_val / 255) * (max_val - min_val)
        return round(raw, decimals)

    # Shape dimensions for Task 1
    shape_tests = {
        "circle": {
            "radius": get_float(0, 3.0, 15.0),
        },
        "rectangle": {
            "width": get_float(1, 2.0, 12.0),
            "height": get_float(2, 2.0, 10.0),
        },
        "square": {
            "side": get_float(3, 2.0, 10.0),
        },
        "triangle": {
            "side_a": get_float(4, 3.0, 8.0),
            "side_b": get_float(5, 4.0, 9.0),
            "side_c": get_float(6, 5.0, 10.0),
        },
    }

    # Precompute expected areas and perimeters
    import math

    r = shape_tests["circle"]["radius"]
    shape_tests["circle"]["expected_area"] = round(math.pi * r * r, 4)
    shape_tests["circle"]["expected_perimeter"] = round(2 * math.pi * r, 4)

    w, h = shape_tests["rectangle"]["width"], shape_tests["rectangle"]["height"]
    shape_tests["rectangle"]["expected_area"] = round(w * h, 4)
    shape_tests["rectangle"]["expected_perimeter"] = round(2 * (w + h), 4)

    s = shape_tests["square"]["side"]
    shape_tests["square"]["expected_area"] = round(s * s, 4)
    shape_tests["square"]["expected_perimeter"] = round(4 * s, 4)

    # Triangle: use Heron's formula for area
    a, b, c = (shape_tests["triangle"]["side_a"],
               shape_tests["triangle"]["side_b"],
               shape_tests["triangle"]["side_c"])
    # Ensure valid triangle (sum of two sides > third)
    # Adjust if necessary
    if a + b <= c:
        c = a + b - 0.5
        shape_tests["triangle"]["side_c"] = round(c, 2)
    if a + c <= b:
        b = a + c - 0.5
        shape_tests["triangle"]["side_b"] = round(b, 2)
    if b + c <= a:
        a = b + c - 0.5
        shape_tests["triangle"]["side_a"] = round(a, 2)

    semi = (a + b + c) / 2
    triangle_area = math.sqrt(semi * (semi - a) * (semi - b) * (semi - c))
    shape_tests["triangle"]["expected_area"] = round(triangle_area, 4)
    shape_tests["triangle"]["expected_perimeter"] = round(a + b + c, 4)

    # Payment amounts for Task 2 (Strategy Pattern)
    payment_tests = {
        "amounts": [
            get_float(7, 10.0, 100.0),
            get_float(8, 50.0, 500.0),
            get_float(9, 100.0, 1000.0),
        ],
        "credit_card_fee_percent": get_float(10, 2.0, 4.0, 1),
        "paypal_fee_percent": get_float(11, 2.5, 3.5, 1),
        "crypto_discount_percent": get_float(12, 1.0, 5.0, 1),
    }

    # Calculate expected totals after fees/discounts
    payment_tests["expected_credit_card"] = [
        round(amt * (1 + payment_tests["credit_card_fee_percent"] / 100), 2)
        for amt in payment_tests["amounts"]
    ]
    payment_tests["expected_paypal"] = [
        round(amt * (1 + payment_tests["paypal_fee_percent"] / 100), 2)
        for amt in payment_tests["amounts"]
    ]
    payment_tests["expected_crypto"] = [
        round(amt * (1 - payment_tests["crypto_discount_percent"] / 100), 2)
        for amt in payment_tests["amounts"]
    ]

    # Event types for Task 4 (Observer Pattern)
    event_options = [
        "user_login", "user_logout", "data_update", "notification",
        "error", "warning", "info", "debug", "purchase", "refund",
        "click", "hover", "submit", "load", "unload", "resize"
    ]

    # Select 4 event types deterministically
    selected_events = []
    for i in range(4):
        idx = get_value(13 + i, 0, len(event_options) - 1)
        event = event_options[idx]
        if event not in selected_events:
            selected_events.append(event)
        else:
            # Pick next available
            for e in event_options:
                if e not in selected_events:
                    selected_events.append(e)
                    break

    observer_tests = {
        "event_types": selected_events[:4] if len(selected_events) >= 4 else selected_events + ["custom_event"] * (4 - len(selected_events)),
        "emit_counts": [get_value(17, 1, 5), get_value(18, 2, 6), get_value(19, 1, 4)],
        "test_payloads": [
            {"id": get_value(20, 100, 999), "message": f"test_{student_id[:8]}"},
            {"value": get_float(21, 1.0, 100.0), "active": get_value(22, 0, 1) == 1},
        ],
    }

    # Composition test values for Task 3
    composition_tests = {
        "vehicle_types": ["Car", "Boat", "Plane"],
        "features": ["Engine", "Wheels", "Wings", "Propeller"],
        "test_combinations": [
            {"vehicle": "Car", "features": ["Engine", "Wheels"]},
            {"vehicle": "Boat", "features": ["Engine", "Propeller"]},
            {"vehicle": "Plane", "features": ["Engine", "Wings"]},
        ],
    }

    return {
        "student_id": student_id,
        "lab": "lab04-oop-design",
        "shape_tests": shape_tests,
        "payment_tests": payment_tests,
        "observer_tests": observer_tests,
        "composition_tests": composition_tests,
        "generated_at": None,  # Will be set when saving
    }


def save_variant(variant: dict, output_path: Path) -> None:
    """Save variant configuration to JSON file."""
    from datetime import datetime, timezone

    variant["generated_at"] = datetime.now(timezone.utc).isoformat()

    with open(output_path, "w") as f:
        json.dump(variant, f, indent=2)

    print(f"Variant configuration saved to: {output_path}")


def main():
    """Generate and save variant configuration."""
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py johndoe123")
        sys.exit(1)

    student_id = sys.argv[1].strip()
    if not student_id:
        print("Error: Student ID cannot be empty")
        sys.exit(1)

    # Generate variant
    variant = generate_variant(student_id)

    # Save to repo root
    repo_root = Path(__file__).parent.parent
    output_path = repo_root / ".variant_config.json"

    save_variant(variant, output_path)

    # Print summary
    print(f"\nGenerated variant for student: {student_id}")
    print(f"Circle radius: {variant['shape_tests']['circle']['radius']}")
    print(f"Rectangle: {variant['shape_tests']['rectangle']['width']} x {variant['shape_tests']['rectangle']['height']}")
    print(f"Payment amounts: {variant['payment_tests']['amounts']}")
    print(f"Event types: {variant['observer_tests']['event_types']}")


if __name__ == "__main__":
    main()
