import pytest
import math

class TestShapes:
    def test_circle_area(self):
        from src.task1_shapes import Circle
        c = Circle(5)
        assert abs(c.area() - 78.54) < 0.01
    
    def test_rectangle_area(self):
        from src.task1_shapes import Rectangle
        r = Rectangle(4, 3)
        assert r.area() == 12
    
    def test_square_inherits_rectangle(self):
        from src.task1_shapes import Square, Rectangle
        s = Square(5)
        assert isinstance(s, Rectangle)
        assert s.area() == 25
    
    def test_total_area_polymorphism(self):
        from src.task1_shapes import Circle, Rectangle, total_area
        shapes = [Circle(1), Rectangle(2, 3)]
        total = total_area(shapes)
        expected = math.pi + 6
        assert abs(total - expected) < 0.01
