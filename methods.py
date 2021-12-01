import datetime as dt


def greet(yourName):
    # Get hour of the day
    # and use it to greet the user accordingly
    currentHour = dt.datetime.today().hour

    if(20 <= currentHour or 6 >= currentHour):
        return "¡Buenas noches "    + yourName + "!"
    if(6 <= currentHour <= 12):
        return "¡Buenos días "      + yourName + "!"
    if(12 <= currentHour <= 20):
        return "¡Buenas tardes "    + yourName + "!"


def reverseEcho(str):
    return ''.join(reversed(str))


def palyndrome(str):
    if(str == ''.join(reversed(str))): return True
    return False