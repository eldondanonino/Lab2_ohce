from methods import palyndrome
import sys


class Console:
    name = sys.argv[1]
    input = None

    def readInput(self) -> str:
        self.action = input()
        if(self.action == "Stop!"):
            return "stop"
        if(palyndrome(self.action)):
            return "palyndrome"
        return "ohce"

#a