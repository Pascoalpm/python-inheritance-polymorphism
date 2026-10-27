from src.zadanie1.car_lorry import Car, Lorry

def test_car_init() -> None:
    car = Car("Toyota", 4, 150)
    assert car.brand == "Toyota"
    assert car.power == 150

def test_lorry_inheritance() -> None:
    lorry = Lorry("Volvo", 6, 400, 20)
    assert isinstance(lorry, Car)
    assert lorry.capacity == 20

def test_lorry_power_change() -> None:
    lorry = Lorry("Volvo", 6, 400, 20)
    lorry.power = 500
    assert lorry.power == 500
