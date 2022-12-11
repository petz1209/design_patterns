
"""
User Story: As a client I want to build 5 different types of vehicles:
1. Audi A3   2. Porsche    3. VW Golf     4. Vito    5.

Flow: 1) Select what you want to build
"""


class Vehicle:
    def __init__(self, v_type: str, name: str, ps: int, wheels: int, color: str, top_speed: int):
        self.v_type = v_type
        self.name = name
        self.ps = ps
        self.wheels = wheels
        self.color = color
        self.top_speed = top_speed

    def drive(self, km):
        print(f"{self.name} takes {int(km/self.top_speed)} hours to drive {km} kilometers")


class VehicleManual:
    def __init__(self, v_type: str, name: str, ps: int, wheels: int, color: str, top_speed: int):
        self.v_type = v_type
        self.name = name
        self.ps = ps
        self.wheels = wheels
        self.color = color
        self.top_speed = top_speed

    def read_manual(self):
        print(f"{self.name}:\n"
              f"This {self.v_type} is {self.color} and It has {self.wheels} wheels and {self.ps} ps.")


def client_code():

    print("Please Select the type of car you want to build")

    # print("1. Truck   2. Sports Car    3. PKW     4. Combi    5. Limousine")
    print("  ".join([f"{k}. {v}" for k, v in vehicle_selection.items()]))
    inp = input(": ")
    return inp


def configure_vehicle(inp: str):
    vehicle, manual = None, None
    if inp in vehicle_selection:
        choice = vehicle_selection[inp]
        if choice == "Audi A3":
            vehicle = Vehicle(v_type="Car", name="Audi A3", ps=120, wheels=4,
                              color="black", top_speed=150)
            manual = VehicleManual(v_type="Car", name="Audi A3", ps=120, wheels=4,
                                   color="black", top_speed=150)
        elif choice == "Porsche":
            vehicle = Vehicle(v_type="Car", name="Porsche", ps=280, wheels=4,
                              color="gray", top_speed=190)
            manual = VehicleManual(v_type="Car", name="Porsche", ps=280, wheels=4,
                                   color="gray", top_speed=190)

        if vehicle:
            manual.read_manual()
            vehicle.drive(3000)



if __name__ == '__main__':
    vehicle_selection = {
        "1": "Audi A3",
        "2":  "Porsche",
        "3": "VW Golf",
        "4": "Vito",
        "5": "VW UP"
    }
    choice = client_code()
    configure_vehicle(choice)

