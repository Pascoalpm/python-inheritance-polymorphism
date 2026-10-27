#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car:
    """Базовый класс: машина."""

    def __init__(self, brand: str, cylinders: int, power: float) -> None:
        self._brand = brand
        self._cylinders = cylinders
        self._power = power

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not value:
            raise ValueError("Марка не может быть пустой")
        self._brand = value

    @property
    def power(self) -> float:
        return self._power

    @power.setter
    def power(self, value: float) -> None:
        if value < 0:
            raise ValueError("Мощность не может быть отрицательной")
        self._power = value

    def info(self) -> None:
        print(
            f"Car: {self._brand}, cylinders: {self._cylinders}, "
            f"power: {self._power} HP"
        )

class Lorry(Car):
    """Производный класс: грузовик."""

    def __init__(
        self, brand: str, cylinders: int, power: float, capacity: float
    ) -> None:
        super().__init__(brand, cylinders, power)
        self._capacity = capacity

    @property
    def capacity(self) -> float:
        return self._capacity

    @capacity.setter
    def capacity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Грузоподъёмность не может быть отрицательной")
        self._capacity = value

    def info(self) -> None:
        print(
            f"Lorry: {self._brand}, cylinders: {self._cylinders}, "
            f"power: {self._power} HP, capacity: {self._capacity} tons"
        )

def main() -> None:
    """Демонстрация работы классов."""
    print("Задание 1: Car → Lorry\n")

    car = Car("Toyota", 4, 150)
    car.info()

    car.power = 180
    print(f"После изменения мощности: {car.power} HP")

    lorry = Lorry("Volvo", 6, 400, 20)
    lorry.info()

    lorry.brand = "Scania"
    lorry.capacity = 25
    print("\nПосле изменений:")
    lorry.info()

if __name__ == "__main__":
    main()
