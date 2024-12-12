from abc import ABC, abstractmethod


# Abstract class Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


# Abstract class VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# Фабрика для створення транспортних засобів специфікації US
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


# Фабрика для створення транспортних засобів специфікації EU
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів специфікації US
us_car = us_factory.create_car("Ford", "Mustang")
us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Street 750")

# Створення транспортних засобів специфікації EU
eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_motorcycle = eu_factory.create_motorcycle("Yamaha", "MT-07")

us_car.start_engine()
us_motorcycle.start_engine()
eu_car.start_engine()
eu_motorcycle.start_engine()