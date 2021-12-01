from methods import palyndrome


class Console:
    name = None
    input = None

    def readInput(fake_input, self) -> str:
        self.input = fake_input
        if self.input == "Stop!":
            return "stop"
        if palyndrome(self.input):
            return "palyndrome"
        return "ohce"
