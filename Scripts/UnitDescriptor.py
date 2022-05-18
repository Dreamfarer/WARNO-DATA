import copy
import descriptor
import analyze

def extractUnitDescriptor(subStr, index):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""
    
    while counterChar < len(subStr):

        #New Weapon Type
        if subStr[counterChar:counterChar+17] == "export Descriptor" or counterChar == len(subStr)-1: #We need to include the last entry!!!! Change this
            if counterUnit > 0:

                UnitDescriptor.append(copy.deepcopy(descriptor.unit))

                for keyWord in range(len(UnitDescriptor[index])):
                    UnitDescriptor[index][keyWord] = [UnitDescriptor[index][keyWord][0], analyze.variable(temporaryStr, UnitDescriptor[index][keyWord])]

                index += 1

            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1


def extract(filePath):

    global UnitDescriptor
    UnitDescriptor = []
    
    extractUnitDescriptor(open(filePath,"r").read(), 0)
    
    return UnitDescriptor
