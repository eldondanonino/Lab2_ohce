from classes.FakeDateIndicator import DateIndicator
from classes.FakeConsole import Console
from methods import greet, reverseEcho,palyndrome

indicator = DateIndicator
console = Console


def test_greeting_night():

    actual = indicator.greet("Pablo", 22)
    expected = "¡Buenas noches Pablo!"
    assert actual == expected


def test_greeting_day():

    actual = indicator.greet("Pablo", 11)
    expected = "¡Buenos días Pablo!"
    assert actual == expected


def test_greeting_evening():

    actual = indicator.greet("Pablo", 18)
    expected = "¡Buenas tardes Pablo!"
    assert actual == expected


def test_reverse_console():
    actual = console.readInput("Burrito", console)
    expected = "ohce"
    assert actual == expected


def test_palyndrome_console():
    actual = console.readInput("BurrirruB", console)
    expected = "palyndrome"
    assert actual == expected


def test_stop_console():
    actual = console.readInput("Stop!", console)
    expected = "stop"
    assert actual == expected

def test_reverse_logic():
    actual = reverseEcho("Burrito")
    expected = "otirruB"
    assert actual == expected

def test_palyndrome_logic():
    actual = palyndrome("BurrirruB")
    expected = True
    assert actual == expected

def test_not_palyndrome():
    actual = palyndrome("Taco cat")
    expected = False
    assert actual == expected

#def test_stop_logic(): How to do this test??
 #   actual = reverseEcho("Stop!")
  #  expected = True
   # assert actual == expected

# Barebone test to C/P later
def test_():
    actual = 1
    expected = 1
    assert actual == expected

#with pytest.raises(Error):
#   logic here