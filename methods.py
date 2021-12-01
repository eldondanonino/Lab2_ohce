import datetime as dt


def greet(yourName):
    # Get hour of the day
    currentHour = dt.datetime.today().hour

    if(20 <= currentHour | 6 >= currentHour):
        return "¡Buenas noches" + yourName +" !"