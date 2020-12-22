#this just demonstartes the module/library
from AminoFunctions import AminoFunctions
import sys

if __name__ == "__main__":
    state = 0
    af = AminoFunctions() #object
    while True:

        while state == 0:
            init = input("\033[0;37;40m"+"Type 1 to convert codons to their respective amino acids.\nType 2 to convert amino acids to their potential codons.\nType 3 to convert single character amino acid codes to their full name\nType 4 to conver three character amino acid codes to their full name\nType 5 to convert an anti sense strands to the strand it coded off of (sense strand)\nType anything else to quit\n")
            if init == "1":
                state = 1
                break
            elif init == "2":
                state = 2
                break
            elif init == "3":
                state = 3
                break;
            elif init == "4":
                state = 4
                break
            elif init == "5":
                state = 5
                break
            else:
                state = 69
                break
        
        while state == 1:
            temp = input("Input the messenger RNA codons you want to convert(all non A,C,G,U characters will be removed):\n").lower()
            store = []
            for i in temp:
                if i == 'a' or i == 'u' or i == 'g' or i == 'c':
                    store.append(i)
            length = len(store)
            if length % 3 != 0:
                print("Incorrect amount of codons. You inputted " + str(length))
            else:
                af.CodonToAcid(store, True)
                state = 0

        while state == 2:
            acids = []
            xd = 1;
            while xd == 1:
                temp = input("Input an amino acids you want to convert, one at a time and press enter. When you are done, press enter again:\n").lower()
                if temp == "":
                    break
                else:
                    acids.append(temp)
            af.AcidToCodons(acids, True)
            state = 0
        
        while state == 3:
            code = input("Input the single character codes of the amino acids you want to convert to get their full name.\n(Try to only have the characters for the code, no spaces/commas/etc):\n").lower()
            temp = []
            for i in code:
                if i != ' ' or i != ',' or i != '&':
                    temp.append(i)
            af.SingleCode(temp, True)
            state = 0

        while state == 4:
            code = input("Input the three character code of the amino acids you want to convert to get their full name.\n(Try to only have the characters for the code, no spaces/commas/etc):\n").lower()
            temp = []
            for i in code:
                if i != ' ' or i != ',' or i != '&':
                    temp.append(i)
            if len(temp)%3 != 0:
                print("Incorrect amount of characters. Try again.")
            else:
                af.ThreeCode(temp, True)
                state = 0

        while state == 5:
            mrna = input("Input the anti sense strand that you what to convert to it's sense strand(all non A,C,G,U characters will be removed):\n").lower()
            code = []
            for i in mrna:
                if i == 'a' or i == 'c' or i == 'g' or i == 'u':
                    code.append(i)
            af.sense(mrna, True)
            state = 0
        
        while state == 69:
            input("Thank you for trying out AminoFunctions. Press any key to exit...\n")
            sys.exit()