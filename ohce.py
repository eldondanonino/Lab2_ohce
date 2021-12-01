from classes.Console import Console
from methods import greet, reverseEcho
from classes.Console import Console


def main():
    console = Console
    print(greet(console.name))
    readString = None
    while True:
        readString = console.readInput(console)
        if readString == "stop":
            print("Adios " + console.name)
            break
        if readString == "palyndrome":
            print(console.input + "\n¡Bonita palabra!")
        if readString == "ohce":
            print(reverseEcho(console.input))


main()
