#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Lab 4: OOP Design
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Extract variant values
    shape = variant["shape_tests"]
    payment = variant["payment_tests"]
    observer = variant["observer_tests"]

    # Replace placeholders
    assignment = template

    # Student ID
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])

    # Circle
    assignment = assignment.replace("{{CIRCLE_RADIUS}}", str(shape["circle"]["radius"]))
    assignment = assignment.replace("{{CIRCLE_EXPECTED_AREA}}", str(shape["circle"]["expected_area"]))
    assignment = assignment.replace("{{CIRCLE_EXPECTED_PERIMETER}}", str(shape["circle"]["expected_perimeter"]))

    # Rectangle
    assignment = assignment.replace("{{RECTANGLE_WIDTH}}", str(shape["rectangle"]["width"]))
    assignment = assignment.replace("{{RECTANGLE_HEIGHT}}", str(shape["rectangle"]["height"]))
    assignment = assignment.replace("{{RECTANGLE_EXPECTED_AREA}}", str(shape["rectangle"]["expected_area"]))
    assignment = assignment.replace("{{RECTANGLE_EXPECTED_PERIMETER}}", str(shape["rectangle"]["expected_perimeter"]))

    # Square
    assignment = assignment.replace("{{SQUARE_SIDE}}", str(shape["square"]["side"]))
    assignment = assignment.replace("{{SQUARE_EXPECTED_AREA}}", str(shape["square"]["expected_area"]))

    # Triangle
    assignment = assignment.replace("{{TRIANGLE_SIDE_A}}", str(shape["triangle"]["side_a"]))
    assignment = assignment.replace("{{TRIANGLE_SIDE_B}}", str(shape["triangle"]["side_b"]))
    assignment = assignment.replace("{{TRIANGLE_SIDE_C}}", str(shape["triangle"]["side_c"]))
    assignment = assignment.replace("{{TRIANGLE_EXPECTED_AREA}}", str(shape["triangle"]["expected_area"]))
    assignment = assignment.replace("{{TRIANGLE_EXPECTED_PERIMETER}}", str(shape["triangle"]["expected_perimeter"]))

    # Payment amounts
    assignment = assignment.replace("{{PAYMENT_AMOUNT_1}}", str(payment["amounts"][0]))
    assignment = assignment.replace("{{PAYMENT_AMOUNT_2}}", str(payment["amounts"][1]))
    assignment = assignment.replace("{{PAYMENT_AMOUNT_3}}", str(payment["amounts"][2]))

    # Payment fees
    assignment = assignment.replace("{{CREDIT_CARD_FEE_PERCENT}}", str(payment["credit_card_fee_percent"]))
    assignment = assignment.replace("{{PAYPAL_FEE_PERCENT}}", str(payment["paypal_fee_percent"]))
    assignment = assignment.replace("{{CRYPTO_DISCOUNT_PERCENT}}", str(payment["crypto_discount_percent"]))

    # Expected payment totals
    assignment = assignment.replace("{{EXPECTED_CREDIT_CARD_1}}", str(payment["expected_credit_card"][0]))
    assignment = assignment.replace("{{EXPECTED_PAYPAL_2}}", str(payment["expected_paypal"][1]))
    assignment = assignment.replace("{{EXPECTED_CRYPTO_3}}", str(payment["expected_crypto"][2]))

    # Observer/Event types
    event_types = observer["event_types"]
    assignment = assignment.replace("{{EVENT_TYPES}}", ", ".join(f"`{e}`" for e in event_types))
    assignment = assignment.replace("{{EVENT_TYPE_1}}", event_types[0] if len(event_types) > 0 else "event1")
    assignment = assignment.replace("{{EVENT_TYPE_2}}", event_types[1] if len(event_types) > 1 else "event2")

    # Test payloads
    payloads = observer["test_payloads"]
    assignment = assignment.replace("{{TEST_PAYLOAD_1}}", str(payloads[0]) if len(payloads) > 0 else "{}")
    assignment = assignment.replace("{{TEST_PAYLOAD_2}}", str(payloads[1]) if len(payloads) > 1 else "{}")

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
