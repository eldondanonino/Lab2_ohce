from classes.DateIndicator import DateIndicator


def greet(yourName):
    indicator = DateIndicator

    return indicator.greet(yourName)


def reverseEcho(str):
    return "".join(reversed(str))


def palyndrome(str):
    if str == "".join(reversed(str)):
        return True
    return False
