from abc import ABCMeta, abstractmethod
from typing import List


# build subscriber interface
class ISubscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self, event):
        raise NotImplementedError


# create publisher:
class Publisher:
    subscribers: List[ISubscriber] = list()

    def publish(self, event):
        for subscriber in self.subscribers:
            subscriber.update(event)

    def subscribe(self, subscriber: ISubscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: ISubscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)


# a concrete subscriber
class Person(ISubscriber):

    def __init__(self, name, interests):
        self.name = name
        self.interests = interests

    def update(self, event):
        if event["topic"] in self.interests:
            print(f"{self.name} is happy about the info {event['info']}")


# another concrete subscriber class
class Retailer(ISubscriber):
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def update(self, event):
        if event["topic"] == self.branch:
            print(f"{self.name} needs to act on information {event['info']}")


def main():
    """
    little user story: 2 people and 1 retailer are subsrcibing to publisher
    a bunch of events are published
    retailer unsbscribes
    events are published again
    """

    # Setup Publisher:
    publisher = Publisher()
    # set up a bunch of events
    events = [{"id": 1, "topic": "car", "info": "A new BMW is now avaliable for 10 euro"},
              {"id": 2, "topic": "fashion", "info": "-25% on all jackets"},
              {"id": 3, "topic": "wood", "info": "-34% on timber at hornbach"},
              ]

    # Set up to people
    peter = Person(name="peter", interests=["car", "fashion"])
    franz = Person(name="franz", interests=["car", "wood"])

    # set up a Retailer
    obi = Retailer(name="OBI", branch="wood")
    # subscribe peter and franz to publisher:
    publisher.subscribe(peter)
    publisher.subscribe(franz)
    publisher.subscribe(obi)

    # iterating over events and publish them
    for event in events:
        str = f"eventId: {event['id']} | Topic: {event['topic']}"
        fillup = 100 - len(str)
        str = str + "-" * fillup
        print(str)
        publisher.publish(event)

    # now lets unsubscribe obi
    publisher.unsubscribe(obi)
    for event in events:
        str = f"eventId: {event['id']} | Topic: {event['topic']}"
        fillup = 100 - len(str)
        str = str + "-" * fillup
        print(str)
        publisher.publish(event)


if __name__ == '__main__':
    main()










