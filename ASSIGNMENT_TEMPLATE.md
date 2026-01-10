# Lab 4: Object-Oriented Design and Polymorphism

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Points:** 100

---

## Overview

This lab explores core object-oriented design principles including abstraction, polymorphism, design patterns, and composition vs inheritance. You will implement a shape hierarchy, a payment processing system using the Strategy pattern, demonstrate composition benefits, and create an event system using the Observer pattern.

**Your personalized test values are included below. Your code must pass tests with these specific values.**

---

## Task 1: Shape Hierarchy (25 points)

Implement the Shape abstract base class and concrete shape classes in `src/task1_shapes.py`.

### Requirements

1. **Shape (Abstract Base Class)**
   - Abstract methods: `area()` and `perimeter()`
   - Both methods return `float`

2. **Circle**
   - Constructor: `Circle(radius: float)`
   - Your test radius: **{{CIRCLE_RADIUS}}**
   - Expected area: **{{CIRCLE_EXPECTED_AREA}}**
   - Expected perimeter: **{{CIRCLE_EXPECTED_PERIMETER}}**

3. **Rectangle**
   - Constructor: `Rectangle(width: float, height: float)`
   - Your test dimensions: **{{RECTANGLE_WIDTH}}** x **{{RECTANGLE_HEIGHT}}**
   - Expected area: **{{RECTANGLE_EXPECTED_AREA}}**
   - Expected perimeter: **{{RECTANGLE_EXPECTED_PERIMETER}}**

4. **Square** (inherits from Rectangle)
   - Constructor: `Square(side: float)`
   - Must be an instance of Rectangle
   - Your test side: **{{SQUARE_SIDE}}**
   - Expected area: **{{SQUARE_EXPECTED_AREA}}**

5. **Triangle**
   - Constructor: `Triangle(side_a: float, side_b: float, side_c: float)`
   - Use Heron's formula for area
   - Your test sides: **{{TRIANGLE_SIDE_A}}**, **{{TRIANGLE_SIDE_B}}**, **{{TRIANGLE_SIDE_C}}**
   - Expected area: **{{TRIANGLE_EXPECTED_AREA}}**
   - Expected perimeter: **{{TRIANGLE_EXPECTED_PERIMETER}}**

6. **total_area(shapes: list[Shape]) -> float**
   - Demonstrates polymorphism by summing areas of different shapes

### Example Usage

```python
from src.task1_shapes import Circle, Rectangle, Square, Triangle, total_area

circle = Circle({{CIRCLE_RADIUS}})
print(f"Circle area: {circle.area()}")  # Should be approximately {{CIRCLE_EXPECTED_AREA}}

shapes = [Circle(1), Rectangle(2, 3), Square(4)]
print(f"Total area: {total_area(shapes)}")
```

---

## Task 2: Payment System - Strategy Pattern (30 points)

Implement a payment processing system in `src/task2_payment.py` using the Strategy design pattern.

### Requirements

1. **PaymentStrategy (Abstract Base Class)**
   - Abstract method: `process_payment(amount: float) -> float`
   - Returns the final amount after fees/discounts

2. **CreditCardPayment**
   - Adds a fee of **{{CREDIT_CARD_FEE_PERCENT}}%**
   - Test amount: {{PAYMENT_AMOUNT_1}} -> Expected: {{EXPECTED_CREDIT_CARD_1}}

3. **PayPalPayment**
   - Adds a fee of **{{PAYPAL_FEE_PERCENT}}%**
   - Test amount: {{PAYMENT_AMOUNT_2}} -> Expected: {{EXPECTED_PAYPAL_2}}

4. **CryptoPayment**
   - Applies a discount of **{{CRYPTO_DISCOUNT_PERCENT}}%**
   - Test amount: {{PAYMENT_AMOUNT_3}} -> Expected: {{EXPECTED_CRYPTO_3}}

5. **PaymentProcessor**
   - Constructor: `PaymentProcessor(strategy: PaymentStrategy)`
   - Method: `checkout(amount: float) -> float`
   - Method: `set_strategy(strategy: PaymentStrategy)` to change payment method

### Example Usage

```python
from src.task2_payment import PaymentProcessor, CreditCardPayment, CryptoPayment

processor = PaymentProcessor(CreditCardPayment())
total = processor.checkout({{PAYMENT_AMOUNT_1}})
print(f"Credit card total: {total}")  # Should be {{EXPECTED_CREDIT_CARD_1}}

processor.set_strategy(CryptoPayment())
total = processor.checkout({{PAYMENT_AMOUNT_3}})
print(f"Crypto total: {total}")  # Should be {{EXPECTED_CRYPTO_3}}
```

---

## Task 3: Composition vs Inheritance (25 points)

Demonstrate the "class explosion" problem with inheritance and solve it using composition in `src/task3_composition.py`.

### The Problem

Consider vehicles with features. With inheritance, you might create:
- Car, Boat, Plane
- CarWithEngine, BoatWithEngine, PlaneWithEngine
- CarWithEngineAndWheels, etc.

This leads to exponential class growth!

### Requirements

1. **Feature Classes** (use composition)
   - `Engine` with method `start() -> str` returning "Engine started"
   - `Wheels` with method `roll() -> str` returning "Wheels rolling"
   - `Wings` with method `fly() -> str` returning "Wings deployed"
   - `Propeller` with method `spin() -> str` returning "Propeller spinning"

2. **Vehicle Class**
   - Constructor accepts a list of features
   - Method `describe() -> list[str]` returns list of all feature actions
   - Demonstrates composition over inheritance

### Test Combinations

Your tests will use these combinations:
- Car with: Engine, Wheels
- Boat with: Engine, Propeller
- Plane with: Engine, Wings

### Example Usage

```python
from src.task3_composition import Vehicle, Engine, Wheels, Wings

car = Vehicle([Engine(), Wheels()])
print(car.describe())  # ["Engine started", "Wheels rolling"]

plane = Vehicle([Engine(), Wings()])
print(plane.describe())  # ["Engine started", "Wings deployed"]
```

---

## Task 4: Observer Pattern - Event System (20 points)

Implement an event emitter system in `src/task4_observer.py` using the Observer design pattern.

### Requirements

1. **EventEmitter Class**
   - `on(event: str, callback: Callable)` - Register a callback for an event
   - `off(event: str, callback: Callable)` - Remove a callback for an event
   - `emit(event: str, *args, **kwargs)` - Trigger all callbacks for an event
   - `once(event: str, callback: Callable)` - Register a callback that fires only once

### Your Test Events

Your implementation will be tested with these event types:
{{EVENT_TYPES}}

### Test Payloads

Your tests will use these payloads:
- Payload 1: `{{TEST_PAYLOAD_1}}`
- Payload 2: `{{TEST_PAYLOAD_2}}`

### Example Usage

```python
from src.task4_observer import EventEmitter

emitter = EventEmitter()

def on_login(user_id):
    print(f"User {user_id} logged in")

emitter.on("{{EVENT_TYPE_1}}", on_login)
emitter.emit("{{EVENT_TYPE_1}}", user_id=123)

# Using once - callback only fires one time
emitter.once("{{EVENT_TYPE_2}}", lambda: print("This runs once"))
emitter.emit("{{EVENT_TYPE_2}}")  # Prints message
emitter.emit("{{EVENT_TYPE_2}}")  # Nothing happens
```

---

## Submission Guidelines

1. Implement all tasks in their respective files under `src/`
2. Run tests locally: `pytest tests/visible/ -v`
3. Commit and push your changes
4. Ensure all GitHub Actions tests pass

## Grading

| Task | Points | Description |
|------|--------|-------------|
| Task 1 | 25 | Shape hierarchy with abstraction and polymorphism |
| Task 2 | 30 | Strategy pattern for payment processing |
| Task 3 | 25 | Composition over inheritance demonstration |
| Task 4 | 20 | Observer pattern event system |
| **Total** | **100** | |

---

**Note:** Your test values are unique to you based on your student ID. Do not copy values from other students as your tests will fail.
