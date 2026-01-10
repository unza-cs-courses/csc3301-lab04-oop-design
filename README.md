# Lab 4: Object-Oriented Design and Polymorphism

**CSC3301 Programming Language Paradigms**
**Points:** 100

## Overview

This lab explores core object-oriented design principles including abstraction, polymorphism, design patterns (Strategy and Observer), and composition vs inheritance.

## Getting Started

1. Clone your personal repository
2. Wait for the variant generation workflow to complete (creates `ASSIGNMENT.md`)
3. Read `ASSIGNMENT.md` for your personalized test values
4. Implement the tasks in the `src/` directory
5. Run tests locally: `pytest tests/visible/ -v`
6. Commit and push your changes

## Tasks

### Task 1: Shape Hierarchy (25 points)
Implement abstract Shape base class with Circle, Rectangle, Triangle, Square in `src/task1_shapes.py`.

### Task 2: Payment System with Strategy Pattern (30 points)
PaymentStrategy interface with CreditCard, PayPal, Crypto implementations in `src/task2_payment.py`.

### Task 3: Composition vs Inheritance (25 points)
Demonstrate the class explosion problem and solve with composition in `src/task3_composition.py`.

### Task 4: Observer Pattern Event System (20 points)
Implement EventEmitter with on(), off(), emit(), once() methods in `src/task4_observer.py`.

## Variant System

This assignment uses a **variant system** to provide each student with unique test values. This ensures academic integrity while allowing collaborative learning.

### How It Works

1. **Automatic Generation**: When you accept the assignment via GitHub Classroom, a workflow automatically generates your unique variant based on your GitHub username.

2. **Variant Configuration**: Your personalized values are stored in `.variant_config.json` (auto-generated, do not modify).

3. **Personalized Assignment**: The `ASSIGNMENT.md` file contains your specific test values and expected results.

4. **Test Compatibility**: Tests in `tests/visible/` use fixtures from `conftest.py` that load your variant values, with sensible defaults for template testing.

### Files

| File | Purpose |
|------|---------|
| `.variant_config.json` | Your unique test values (auto-generated) |
| `ASSIGNMENT.md` | Your personalized assignment with specific values |
| `ASSIGNMENT_TEMPLATE.md` | Template with placeholders (for instructors) |
| `scripts/variant_generator.py` | Generates variant from student ID |
| `scripts/generate_assignment.py` | Creates ASSIGNMENT.md from template |
| `tests/visible/conftest.py` | Pytest fixtures that load variant config |

### Variant Values Include

- **Shape Tests**: Unique dimensions for circles, rectangles, squares, and triangles
- **Payment Tests**: Specific amounts and fee percentages for strategy pattern
- **Observer Tests**: Unique event types and payloads for event emitter
- **Composition Tests**: Vehicle and feature combinations

### Running Tests

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run specific task tests
pytest tests/visible/test_lab4.py -v

# Tests automatically use your variant values if .variant_config.json exists
# Otherwise, they use default values (for template testing)
```

### Manual Variant Generation (Instructors Only)

```bash
# Generate variant for a specific student
python scripts/variant_generator.py student_username

# Generate personalized assignment
python scripts/generate_assignment.py
```

## Project Structure

```
csc3301-lab04-oop-design/
├── .github/
│   └── workflows/
│       ├── autograding.yml      # Runs tests on push
│       └── generate-variant.yml # Generates variant on repo creation
├── scripts/
│   ├── variant_generator.py     # Generates .variant_config.json
│   └── generate_assignment.py   # Creates ASSIGNMENT.md
├── src/
│   ├── __init__.py
│   ├── task1_shapes.py          # Shape hierarchy
│   ├── task2_payment.py         # Strategy pattern (create this)
│   ├── task3_composition.py     # Composition demo (create this)
│   └── task4_observer.py        # Observer pattern (create this)
├── tests/
│   ├── __init__.py
│   └── visible/
│       ├── __init__.py
│       ├── conftest.py          # Pytest fixtures with variant values
│       └── test_lab4.py         # Test cases
├── .variant_config.json         # Auto-generated variant config
├── ASSIGNMENT.md                # Auto-generated personalized assignment
├── ASSIGNMENT_TEMPLATE.md       # Template with placeholders
├── README.md                    # This file
└── requirements.txt             # Python dependencies
```

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all tests pass locally
3. Commit and push your changes
4. Verify GitHub Actions shows all tests passing

## Academic Integrity

Your test values are unique to your student ID. Sharing solutions will not help others as their expected values will differ. Focus on understanding the concepts and implementing correct solutions.
