import copy
import descriptor
import analyze

def extractAmmunition(subStr, index):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""
    
    while counterChar < len(subStr):

        #New Weapon Type
        if subStr[counterChar:counterChar+11] == "export Ammo" or counterChar == len(subStr)-1: #We need to include the last entry!!!! Change this
            if counterUnit > 0:

                Ammunition.append(copy.deepcopy(descriptor.ammo))

                for keyWord in range(len(Ammunition[index])):
                    Ammunition[index][keyWord] = [Ammunition[index][keyWord][0], analyze.variable(temporaryStr, Ammunition[index][keyWord])]

                index += 1

            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1


def extract(filePath):

    global Ammunition
    Ammunition = []
    
    extractAmmunition(open(filePath,"r").read(), 0)
    
    return Ammunition
