import sys
from classes.Console import Console
from methods import greet, reverseEcho, palyndrome
from classes.Console import Console


def main():
    print(greet(sys.argv[1]))
    readString = None
    daniil = Console
    while(True):
        readString = daniil.readInput(daniil)
        if(readString == "stop"):
            print("Adios " + daniil.name)
            break
        if(readString == "palyndrome"):
            print(daniil.input + "¡Bonita palabra!")
        if(readString == "ohce"):
            print(reverseEcho(daniil.input))


main()
