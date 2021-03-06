import datetime as dt


class DateIndicator:
    currentHour = None


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
    