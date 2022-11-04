"""Implementing Proxy Pattern
All in one File since it should display how everything comes together
"""
import time
from abc import ABCMeta, abstractmethod


# creating an interface that is implemented by both the actual class and the proxy
class IPeron(metaclass=ABCMeta):
    @abstractmethod
    def get_person_info(self):
        raise NotImplementedError


# class for business logic
class Person(IPeron):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person_info(self):
        # implementation of the interface
        print(f"name: {self.name}")
        print(f"age: {self.age}")


# proxy that wraps business logic implementation of IPerson
class ProxyPerson(IPeron):
    count = 1

    def __init__(self, p: IPeron):
        self.p = p

    def get_person_info(self):
        # interface implementation
        print(f"counter: {self.count}")
        if self.count < 4:
            self.p.get_person_info()
            self.count += 1
        else:
            raise Exception(f"Access Limit 3 was reached")


def main(person: IPeron):
    # calls the person object through the proxy 4 times and gets through until proxy prohibits access
    for _ in range(10):
        person.get_person_info()
        time.sleep(0.2)


if __name__ == '__main__':
    # setup proxy
    proxy = ProxyPerson(Person(name="patrick", age=35))
    # adding that proxy to the business_logic
    main(proxy)


