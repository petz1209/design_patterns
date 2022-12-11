from abc import ABCMeta, abstractmethod
from typing import Optional
"""
User Story: As a client I want to build 5 different types of vehicles:
1. Audi A3   2. Porsche    3. VW Golf     4. Vito    5.VW Up

Flow: 1) Select what you want to build
"""


# Product Class
class Car:
    v_type: Optional[int] = None
    name: Optional[str]  = None
    ps: Optional[int] = None
    wheels: Optional[int] = None
    color: Optional[str] = None
    top_speed: Optional[int] = None

    def drive(self, km):
        print(f"{self.name} takes {int(km/self.top_speed)} hours to drive {km} kilometers")


# Product Class
class Manual:
    v_type: Optional[str] = None
    name: Optional[str] = None
    ps: Optional[int] = None
    wheels: Optional[int] = None
    color: Optional[str] = None
    top_speed: Optional[int] = None

    def __str__(self):
        return f"Manual======================================================\n"\
               f"{self.name}:\n"\
               f"This {self.v_type} is {self.color} and It has {self.wheels} wheels and {self.ps} ps.\n"\
                "======" \
               "======================================================\n"


# Builder Interface
class IBuilder(metaclass=ABCMeta):

    @abstractmethod
    def reset(self):
        raise NotImplementedError
    @abstractmethod
    def build(self):
        raise NotImplementedError
    @abstractmethod
    def set_type(self, _type: str):
        raise NotImplementedError
    @abstractmethod
    def set_name(self, name: str):
        raise NotImplementedError
    @abstractmethod
    def set_ps(self, ps: int):
        raise NotImplementedError
    @abstractmethod
    def set_wheels(self, wheels: int):
        raise NotImplementedError
    @abstractmethod
    def set_color(self, color: str):
        raise NotImplementedError
    @abstractmethod
    def set_speed(self, speed: int):
        raise NotImplementedError


class CarBuilder(IBuilder):

    def __init__(self):
        self._product = Car()

    def reset(self):
        self._product = Car()

    def build(self):
        product = self._product
        self.reset()
        return product

    def set_type(self, _type: str):
        self._product.v_type = _type

    def set_name(self, name: str):
        self._product.name = name

    def set_ps(self, ps: int):
        self._product.ps = ps

    def set_wheels(self, wheels: int):
        self._product.wheels = wheels

    def set_color(self, color: str):
        self._product.color = color

    def set_speed(self, speed: int):
        self._product.top_speed = speed


class ManualBuilder(IBuilder):

    def __init__(self):
        self._product = Manual()

    def reset(self):
        self._product = Manual()

    def build(self):
        product = self._product
        self.reset()
        return product

    def set_type(self, _type: str):
        self._product.v_type = _type

    def set_name(self, name: str):
        self._product.name = name

    def set_ps(self, ps: int):
        self._product.ps = ps

    def set_wheels(self, wheels: int):
        self._product.wheels = wheels

    def set_color(self, color: str):
        self._product.color = color

    def set_speed(self, speed: int):
        self._product.top_speed = speed


class Director:
    """Global director that implements every Car creation as its own method"""

    def build_audi_a3(self, builder: IBuilder):
        builder.set_type("Car")
        builder.set_ps(120)
        builder.set_speed(160)
        builder.set_color("black")
        builder.set_name("Audi A3")
        return builder.build()

    def build_porsche(self, builder: IBuilder):
        builder.set_type("Car")
        builder.set_ps(250)
        builder.set_speed(220)
        builder.set_color("gray")
        builder.set_name("Porsche")
        return builder.build()

    def build_vw_golf(self, builder: IBuilder):
        builder.set_type("Car")
        builder.set_ps(120)
        builder.set_speed(140)
        builder.set_color("blue")
        builder.set_name("VW Golf")
        return builder.build()

    def build_vito(self, builder: IBuilder):
        builder.set_type("Car")
        builder.set_ps(190)
        builder.set_speed(140)
        builder.set_color("black")
        builder.set_name("Mercedes Vito")
        return builder.build()

    def build_vw_up(self, builder: IBuilder):
        builder.set_type("ECar")
        builder.set_ps(90)
        builder.set_speed(100)
        builder.set_color("white")
        builder.set_name("VW UP")
        return builder.build()

    def build_unique_car(self, builder: IBuilder, configs: dict):
        builder.set_type(configs["type"])
        builder.set_ps(configs["ps"])
        builder.set_speed(configs["top_speed"])
        builder.set_color(configs["color"])
        builder.set_name(configs["name"])

# Alternative: Build a Director for each type of car




def client_code():

    print("Please Select the type of car you want to build")

    # print("1. Truck   2. Sports Car    3. PKW     4. Combi    5. Limousine")
    print("  ".join([f"{k}. {v}" for k, v in vehicle_selection.items()]))
    inp = input(": ")
    return inp


class VehicleFactory:

    def create(self, choice):
        director = Director()
        if choice == "Audi A3":
            return director.build_audi_a3
        elif choice =="Porsche":
            return director.build_audi_a3
        elif choice =="VW Golf":
            return director.build_vw_golf
        elif choice == "Vito":
            return director.build_vito
        elif choice == "VW UP":
            return director.build_vito


def unique_config():
    car_builder = CarBuilder()
    man_builder = ManualBuilder()
    name = input("set name: ")
    car_builder.set_name(name)
    man_builder.set_name(name)
    _type = input("set type: ")
    car_builder.set_type(_type)
    man_builder.set_type(_type)
    ps = int(input("set ps: "))
    car_builder.set_ps(ps)
    man_builder.set_ps(ps)
    wheels = int(input("set wheels: "))
    car_builder.set_wheels(wheels)
    man_builder.set_wheels(wheels)
    color = input("set color: ")
    car_builder.set_color(color)
    man_builder.set_color(color)
    top_speed = int(input("set topspeed: "))
    car_builder.set_speed(top_speed)
    man_builder.set_speed(top_speed)
    car = car_builder.build()
    manual = man_builder.build()
    return car, manual


def configure_vehicle(inp: str):
    if inp in vehicle_selection and inp != "6":
        choice = vehicle_selection[inp]

        car_builder = CarBuilder()
        build_fn = VehicleFactory().create(choice)
        vehicle = build_fn(car_builder)
        manual_builder = ManualBuilder()
        manual = build_fn(manual_builder)
    else:
        vehicle, manual = unique_config()

    print(manual)
    vehicle.drive(3000)

if __name__ == '__main__':

    vehicle_selection = {
        "1": "Audi A3",
        "2": "Porsche",
        "3": "VW Golf",
        "4": "Vito",
        "5": "VW UP",
        "6": "Manual Configuration"
    }
    inp =client_code()
    configure_vehicle(inp)
