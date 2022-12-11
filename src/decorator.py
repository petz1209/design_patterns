

from abc import ABC, ABCMeta, abstractmethod


# Interface for Notifiers
class INotifier(metaclass=ABCMeta):
    @abstractmethod
    def send_message(self, message):
        raise NotImplementedError


# A concrete Notifier
class Notifier(INotifier):
    _type = "SMS"

    def send_message(self, message):
        print(f"SMS notify: {message}")


# An Abstract Base notifier for Notifiers
class BaseDecorator(ABC, INotifier):
    def __init__(self, wrappee: INotifier):
        self.wrappee = wrappee

    @abstractmethod
    def send_message(self, message):
        self.wrappee.send_message(message)


# Concrete Email Decoration for notifier
class EmailDecorator(BaseDecorator):
    _type = "eMail"

    def send_message(self, message):
        self.wrappee.send_message(message)
        print(f"Email notify: {message}")


# Concrete Slack Decoration for notifier
class SlackDecorator(BaseDecorator):
    _type = "eMail"

    def send_message(self, message):
        self.wrappee.send_message(message)
        print(f"Slack notify: {message}")


# Setting up a factory to decorate the notifier
class NotifierFactory:

    def create_notifier(self, notifier_type: str) -> INotifier:
        if notifier_type == "sms":
            return self._create_regular_notifier()
        else:
            return self._create_all_notifiers()

    def _create_regular_notifier(self):
        return Notifier()

    def _create_all_notifiers(self):
        return SlackDecorator(
            EmailDecorator(
                Notifier()
            )
        )


def client_code():

    notifier_type = "all"
    message = "hello world"

    notifier = NotifierFactory().create_notifier(notifier_type)
    notifier.send_message(message)


def main():
    client_code()


if __name__ == '__main__':
    main()

    """
    notifier_plattforms = {"email": EmailDecorator,
                           "slack": SlackDecorator
                           }

    message = "hello word"
    services = ["email", "slack"]
    notifier = Notifier()
    for service in services:
        if service in notifier_plattforms:
            notifier = notifier_plattforms[service](notifier)
    notifier.send_message(message)
    """



