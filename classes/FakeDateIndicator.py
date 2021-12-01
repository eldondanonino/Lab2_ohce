class DateIndicator:
    currentHour = None

    def greet(fake_input, currentHour):
        # Get hour of the day
        # and use it to greet the user accordingly

        if 20 <= currentHour or 6 >= currentHour:
            return "¡Buenas noches " + fake_input + "!"
        if 6 <= currentHour <= 12:
            return "¡Buenos días " + fake_input + "!"
        if 12 <= currentHour <= 20:
            return "¡Buenas tardes " + fake_input + "!"
