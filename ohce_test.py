from classes.FakeDateIndicator import DateIndicator

def test_greeting_night():
    indicator = DateIndicator
    actual =  indicator.greet("Pablo",22)
    expected = "¡Buenas noches Pablo!"
    assert actual == expected

def test_greeting_day():
    indicator = DateIndicator
    actual =  indicator.greet("Pablo",11)
    expected = "¡Buenos días Pablo!"
    assert actual == expected

def test_greeting_evening():
    indicator = DateIndicator
    actual =  indicator.greet("Pablo",18)
    expected = "¡Buenas tardes Pablo!"
    assert actual == expected








#Barebone test to C/P later
def test_():
    actual = 1
    expected = 1
    assert actual == expected