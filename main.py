#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.zadanie1 import car_lorry
from src.zadanie2 import figures

def main() -> None:
    print("ЛАБОРАТОРНАЯ РАБОТА 4")

    while True:
        print("\nВыберите задание:")
        print("1 — Задание 1: Car → Lorry")
        print("2 — Задание 2: Фигуры (Figure)")
        print("0 — Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            print()
            car_lorry.main()
        elif choice == "2":
            print()
            figures.main()
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("\nОшибка: неверный выбор.")

if __name__ == "__main__":
    main()
