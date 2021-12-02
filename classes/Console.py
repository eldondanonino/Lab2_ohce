from methods import palyndrome
import sys


class Console:
    try:
        name = sys.argv[1]
    except IndexError:
        print("Please input a name when calling the script, your name will be set to Bob as default")
        name = "Bob"
    input = None

    def readInput(self) -> str:
        self.input = input()
        if self.input == "Stop!":
            return "stop"
        if palyndrome(self.input):
            return "palyndrome"
        return "ohce"
