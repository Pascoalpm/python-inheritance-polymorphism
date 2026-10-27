import math

from src.zadanie2.figures import Circle, Figure, Rectangle

def test_rectangle_area() -> None:
    rect = Rectangle(10, 5)
    assert rect.area() == 50
    assert rect.perimeter() == 30

def test_circle_area() -> None:
    circle = Circle(5)
    assert abs(circle.area() - math.pi * 25) < 0.001

def test_figure_polymorphism() -> None:
    rect = Rectangle(10, 5)
    assert isinstance(rect, Figure)
