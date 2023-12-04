from datetime import datetime


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        current_year = datetime.now().year
        if 1900 <= year <= current_year:
            self.year = year
        else:
            raise ValueError(f"Invalid year {year}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency/100  # ex: fuel_efficiency = 8 -> 8L/100km

    def calculate_fuel_consumption(self, distance):
        return self.fuel_efficiency * distance


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed  # km per hour

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, Top Speed: {self.top_speed} km/h"


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity  # NM

    def calculate_towing_capacity(self):
        return self.towing_capacity


def main():
    # Example usage:
    car = Car("Toyota", "Camry", 2022, fuel_efficiency=8)
    car_mileage = car.calculate_fuel_consumption(100)
    print(f"{car.year} {car.make} {car.model}, Fuel consumed/expended: {car_mileage:.2f} L")

    motorcycle = Motorcycle("Marine Turbine Technologies", "420-rr", 2020, top_speed=439.35091)
    # the fastest as of today: 02.12.2023 22:39
    print(motorcycle.display_info())

    truck = Truck("Ford", "F-150 Raptor", 2023, towing_capacity=2500)
    truck_towing_capacity = truck.calculate_towing_capacity()
    print(f"{truck.year} {truck.make} {truck.model}, Towing Capacity: {truck_towing_capacity} kilograms")


if __name__ == "__main__":
    main()