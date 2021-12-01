import datetime as dt


def greet(yourName):
    # Get hour of the day
    currentHour = dt.datetime.today().hour

    if(20 <= currentHour or 6 >= currentHour):
        return "¡Buenas noches " + yourName + "!"
    if(6 <= currentHour <= 12):
        return "¡Buenos días " + yourName + "!"
    if(12 <= currentHour <= 20):
        return "¡Buenas tardes " + yourName + "!"


def detectWord(word: str) -> str:
    return 'sku'
