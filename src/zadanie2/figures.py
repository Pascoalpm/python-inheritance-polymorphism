#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный базовый класс: фигура."""

    def __init__(self, name: str = "Figure") -> None:
        self._name = name

    @abstractmethod
    def area(self) -> float:
        """Абстрактный метод: площадь."""
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """Абстрактный метод: периметр."""
        ...

    def info(self) -> None:
        print(
            f"{self._name}: area = {self.area():.2f}, "
            f"perimeter = {self.perimeter():.2f}"
        )

class Rectangle(Figure):
    """Прямоугольник."""

    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

class Circle(Figure):
    """Круг."""

    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

class Trapezium(Figure):
    """Трапеция."""

    def __init__(
        self, a: float, b: float, h: float, c: float, d: float
    ) -> None:
        super().__init__("Trapezium")
        self._a = a
        self._b = b
        self._h = h
        self._c = c
        self._d = d

    def area(self) -> float:
        return (self._a + self._b) * self._h / 2

    def perimeter(self) -> float:
        return self._a + self._b + self._c + self._d

def main() -> None:
    """Демонстрация полиморфизма."""
    print("Задание 2: Абстрактный класс Figure\n")

    figures = [
        Rectangle(10, 5),
        Circle(7),
        Trapezium(6, 4, 3, 5, 5),
    ]

    for fig in figures:
        fig.info()

    print("\nПроверка isinstance")
    for fig in figures:
        print(f"{fig._name} is Figure: {isinstance(fig, Figure)}")

if __name__ == "__main__":
    main()
