"""
Lab 4 Task 1: Shape Hierarchy
Implement the Shape abstract base class and concrete shapes.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate area."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter."""
        pass

class Circle(Shape):
    """Circle shape."""
    # YOUR CODE HERE
    pass

class Rectangle(Shape):
    """Rectangle shape."""
    # YOUR CODE HERE
    pass

class Square(Rectangle):
    """Square - special case of Rectangle."""
    # YOUR CODE HERE
    pass

class Triangle(Shape):
    """Triangle with three sides."""
    # YOUR CODE HERE
    pass

def total_area(shapes: list[Shape]) -> float:
    """Calculate total area of all shapes (polymorphism demo)."""
    # YOUR CODE HERE
    pass
