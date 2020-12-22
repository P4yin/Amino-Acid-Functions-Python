from datetime import datetime #needed for file names
class AminoFunctions:

    _acids = { #dictionary for speed
        "alanine": "GCU, GCC, GCA, GCG", #omg gcc
        "arginine": "CGU, CGC, CGA, CGG, AGA, AGG",
        "asparagine": "AAU, AAC",
        "aspartic acid": "GAU, GAC",
        "cysteine": "UGU, UGC",
        "glutamine": "CAA, CAG",
        "glutamic acid": "GAA, GAG",
        "glycine": "GGU, GGC, GGA, GGG",
        "histidine": "CAU, CAC",
        "isoleucine": "AUU, AUC, AUA",
        "leucine": "UUA, UUG, CUU, CUC, CUA, CUG",
        "lysine": "AAA, AAG",
        "methionine": "AUG",
        "phenylalanine": "UUU, UUC",
        "proline": "CCU, CCC, CCA, CCG",
        "serine": "UCU, UCC, UCA, UCG, AGU, AGC",
        "threonine": "ACU, ACC, ACA, ACG",
        "tryptophan": "UGG",
        "tyrosine": "UAU, UAC",
        "valine": "GUU, GUC, GUA, GUG",
        "pyrrolysine": "UAG",
        "selenocysteine": "UGA",
        "stop": "UAG, UAA, UGA"
    }
    _codes = { #dictionary for codes
        "a":"alanine",
        "r":"arginine",
        "n":"asparagine",
        "d":"aspartic acid",
        "c":"cysteine",
        "q":"glutamine",
        "e":"glutamic acid",
        "g":"glycine",
        "h":"histidine",
        "i":"isoleucine",
        "l":"leucine",
        "k":"lysine",
        "m":"methionine",
        "f":"phenylalanine",
        "p":"proline",
        "s":"serine",
        "t":"threonine",
        "w":"tryptophan",
        "y":"tyrosine",
        "v":"valine",
        "u":"selenocysteine",
        "o":"pyrrolysine"
    }
    _3codes = {
        "ala":"alanine",
        "arg":"arginine",
        "asn":"asparagine",
        "asp":"aspartic acid",
        "cys":"cysteine",
        "gln":"glutamine",
        "glu":"glutamic acid",
        "gly":"glycine",
        "his":"histidine",
        "ile":"isoleucine",
        "leu":"leucine",
        "lys":"lysine",
        "met":"methionine",
        "phe":"phenylalanine",
        "pro":"proline",
        "ser":"serine",
        "thr":"threonine",
        "trp":"tryptophan",
        "tyr":"tyrosine",
        "val":"valine",
        "sec":"selenocysteine",
        "pyl":"pyrrolysine"
    }
    _sense = { # i think dictionarys are faster ?
        "a": "T",
        "u": "A",
        "c": "G",
        "g": "C"
    }
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # the varible S is if you want the results to be printed out in the command line or not.
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def CodonToAcid(self, codon, s): # converts an inputted string of codons to their respective amino acids. 
        # parameters
        # codons: the inputted mrna codons (string)
        # s: true/false if you want to print a ton of stuff to command line (boolean)
        print("\n")
        day = datetime.now()
        file_name = day.strftime("%d-%m-%Y_%H-%M-%S" + "acids" +".txt")
        f = open(file_name, "w")
        a = 0
        b = 1
        c = 2
        x = []
        lim = int(len(codon)/3)

        for i in codon:
            x.append(i)

        for i in range(lim):
            if x[a] == 'u':
                if x[b] == 'u':
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Phenylalanine"
                    else:
                        acid = "Leucine"
                elif x[b] == 'c':
                    acid = "Serine"
                elif x[b] == 'a':
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Tyrosine"
                    elif x[c] == 'g':
                        acid = "STOP (Pyrrolysine)"
                    else:
                        acid = "STOP"
                else:
                    if x[c] == 'g':
                        acid = "Tryptophan"
                    elif x[c] == 'a':
                        acid = "STOP (Selenocysteine)"
                    else:
                        acid = "Cysteine"
			
            elif x[a] == 'c':
                if x[b] == 'u':
                    acid = "Leucine"
                elif x[b] == 'c':
                    acid = "Proline"		
                elif x[b] == 'a':
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Histidine"
                    else:
                        acid = "Glutamine"
                else:
                    acid = "Arginine"

            elif x[a] == 'a':
                if x[b] == 'u':
                    if x[c] == 'g':
                        acid = "Methionine"
                    else:
                        acid = "Isoleucine"
                elif x[b] == 'c':
                    acid = "Threonine"
                elif x[b] == 'a':
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Asparagine"
                    else:
                        acid = "Lysine"
                else:
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Serine"
                    else:
                        acid = "Arginine"

            else:
                if x[b] == 'u':
                    acid = "Valine"
                elif x[b] == 'c':
                    acid = "Alanine"
                elif x[b] == 'a':
                    if x[c] == 'u' or x[c] == 'c':
                        acid = "Aspartic acid"
                    else:
                        acid = "Glutamic acid"
                else:
                    acid = "Glycine"
            if s == True:
                print("The codon " +x[a].upper()+x[b].upper()+x[c].upper() + " makes " +acid.upper())
            f.write(acid + "\n")
            a+=3
            b+=3
            c+=3
        f.close()
        print("Created a file " + file_name + " that contains the acids. File format is D/M/Y and H:M:S\n")
    
    def AcidToCodons(self, acid, s): # converts amino acids to their respective codon(s). Uses the acids dictionary. 
        #parameters
        #acid: the inputted amino acids (list)
        # s: true/false if you want to print a ton of stuff to command line (boolean)
        print("\n")
        day = datetime.now()
        file_name = day.strftime("%d-%m-%Y_%H-%M-%S" + "codons" +".txt")
        f = open(file_name, "w")
        for i in acid:
            codons = self._acids.get(i)
            if codons != None:
                f.write(i + ": " + codons + "\n")
                if s == True:
                    print("The amino acid " + i.upper() + " could be " + codons)
            else:
                print("The amino acid" + i.upper() + "does not exist")
        f.close()
        print("Created a file " + file_name + " that contains the codons. File format is D/M/Y and H:M:S\n")

    def SingleCode(self, code, s): #converts single character codes to their respective acids. Uses a code dictionary. I
        #parameters
        #code: inputted single character codes (list/string)
        # s: true/false if you want to print a ton of stuff to command line (boolean)
        print("\n")
        for i in code:
            acid = self._codes.get(i)
            if acid != None:
                if s == True:
                    print("The code " + i.upper() + " is " + acid.upper())
            else: 
                print("The code " + i.upper() + " does not exist.")

    def ThreeCode(self, code, s): #convers 3 character codes to their respective amino acids
        #parameters
        #code: inputted codes (string)
        # s: true/false if you want to print a ton of stuff to command line (boolean)
        print("\n")
        a = 0
        b = 1
        c = 2
        for i in range(int (len(code)/3)):
            three = code[a]+code[b]+code[c]
            acid = self._3codes.get(three)
            if acid != None:
                if s == True:
                    print("The code " + three.upper() + " is " + acid.upper())
            else: 
                print("The code " + three.upper() + " does not exist.")
            a+=3
            b+=3
            c+=3
    
    def sense(self, mrna, s):#takes antisense string and finds its sense string
        #parameters
        #mrna: antisense string(string)
        # s: true/false if you want to print a ton of stuff to command line (boolean)
        print("\n")
        day = datetime.now()
        file_name = day.strftime("%d-%m-%Y_%H-%M-%S" + "sense" +".txt")
        sense = ""
        for i in mrna:
            temp = self._sense.get(i)
            sense+=temp
        if s == True:
            print("The mRNA chain of:\n" + mrna.upper()+ "\nhas the sense strand of:\n" +sense)
        f = open(file_name, "w")
        f.write("anti-sense:" + mrna + "\n" + "sense:" + sense)
        f.close()
        print("Created file " + file_name + " that contains the sense strand and anti sense strand. File format is D/M/Y and H:M:S\n")