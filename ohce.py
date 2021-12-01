import sys
from classes.Console import Console
from methods import greet, reverseEcho, palyndrome
from classes.Console import Console


def main():
    daniil = Console
    print(greet(daniil.name))
    readString = None
    while(True):
        readString = daniil.readInput(daniil)
        if(readString == "stop"):
            print("Adios " + daniil.name)
            break
        if(readString == "palyndrome"):
            print(daniil.input + "\n¡Bonita palabra!")
        if(readString == "ohce"):
            print(reverseEcho(daniil.input))


main()
