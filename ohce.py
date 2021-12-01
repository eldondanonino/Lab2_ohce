import sys
from classes.Console import Console
from methods import greet, reverseEcho, palyndrome
from classes.Console import Console


def main():
        print(greet(sys.argv[1]))

        daniil = ""
        while(True):       
                daniil = input()
                if(daniil == "Stop!"): break

                if(palyndrome(daniil)):
                        print(daniil)
                        print("¡Bonita palabra!")
                else:
                        print(reverseEcho(daniil))
                        

        print("Adios " + sys.argv[1])


main()