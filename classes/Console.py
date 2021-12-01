from methods import palyndrome
import sys


class Console:
    name = sys.argv[1]
    input = None

    def readInput(self) -> str:
        self.input = input()
        if self.input == "Stop!":
            return "stop"
        if palyndrome(self.input):
            return "palyndrome"
        return "ohce"
