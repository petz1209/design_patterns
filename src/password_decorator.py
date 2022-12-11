from abc import ABCMeta, ABC, abstractmethod


class IPassword(metaclass=ABCMeta):
    def set_password(self, password: str) -> str or False:
        raise NotImplementedError


class PasswordSetter(IPassword):

    def set_password(self, password: str) -> str or False:
        return password


class PasswordBaseDecorator(IPassword, ABC):

    def __init__(self, wrappee: IPassword):
        self.wrappee = wrappee

    def set_password(self, password: str) -> str or False:
        raise NotImplementedError


class PasswordNumberDecorator(PasswordBaseDecorator):

    def set_password(self, password: str) -> str or False:
        # check if a number is in password:
        if any(char.isdigit() for char in password):
            return self.wrappee.set_password(password)
        else:
            print("No number in this password")
            return False


class PasswordUpperCaseDecorator(PasswordBaseDecorator):

    def set_password(self, password: str) -> str or False:
        if any(char.isupper() for char in password):
            return self.wrappee.set_password(password)
        else:
            print("No uppercase character in password")
            return False


class PasswordSpecialCharsDecorator(PasswordBaseDecorator):

    def set_password(self, password: str) -> str or False:
        specials = ["!", "?", "#"]
        exists = False
        for special in specials:
            if special in password:
                exists = True
                return self.wrappee.set_password(password)
        if not exists:
            print("No special character in password")
            return exists


def set_password_safety_measures() -> list:

    safetychecks = list()
    types_list  = {"1": "numbers check",
                   "2": "uppercase check",
                   "3": "specialchar check"
                   }
    print("define your password prerequisits")
    print("[1] contain number [2] One UpperCase [3] Contain any(?!;#)")
    while True:
        print(f"selected safety checks: {', '.join([x for x in safetychecks])}")
        selected = input("select: ")
        if (selected in types_list) and (types_list[selected] not in safetychecks):
            safetychecks.append(types_list[selected])
        if selected == "0":
            break
    return safetychecks


def input_password():
    print("Please enter the password")
    pw = input("enter:  ")
    return pw


def main():
    decorators = {"numbers check": PasswordNumberDecorator,
                  "uppercase check": PasswordUpperCaseDecorator,
                  "specialchar check": PasswordSpecialCharsDecorator
                  }

    safety_checks = list()
    safety_checks = set_password_safety_measures()
    pw = input_password()

    pw_validate = PasswordSetter()
    for decorator in safety_checks:
        if decorator in decorators:
            pw_validate = decorators[decorator](pw_validate)
    password = pw_validate.set_password(pw)
    if password:
        print("Password is valid")









if __name__ == '__main__':
    main()
