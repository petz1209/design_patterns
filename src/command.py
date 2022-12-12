from typing import List
from dataclasses import dataclass
import dataclasses
from abc import ABCMeta, abstractmethod
import os


class ICommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


@dataclass
class BuildHouseCommand(ICommand):
    """Command Implementation"""

    material: str
    size: int

    def __dict__(self) -> dict:
        return {"material": self.material, "size": self.size}
    def execute(self):
        print(f"Build a {self.material} House with size {self.size}")


@dataclass
class GetIceCreamCommand(ICommand):
    """Spezific Command + executer"""
    scoops: int
    flavors: List[str]

    def __dict__(self) -> dict:
        return {"scoops": self.scoops, "flavors": self.flavors}
    def execute(self):
        print(f"Got an Icream with {self.scoops} Scoops.\nI got the following flavors:{', '.join([f for f in self.flavors])}")


class CommandFactory:
    """Decides What type of command should be ran and consumes the parameters"""
    def create(self, params) -> ICommand:
        if params["command"] == "get icecream":
            return self.set_params(GetIceCreamCommand, params)
        elif params["command"] == "build house":
            return self.set_params(BuildHouseCommand, params)

    def set_params(self, _class: dataclass, params: dict) -> ICommand:
        field_names = set(f.name for f in dataclasses.fields(_class))
        return _class(**{k: v for k, v in params.items() if k in field_names})


class Worker:
    """Worker executes jobs if it exists"""

    _job = None

    def set_job(self, command: ICommand):
        self._job = command

    def run(self):
        if isinstance(self._job, ICommand):
            self._job.execute()
