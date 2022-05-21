import copy
import descriptor
import analyze

def extractOrderAvailability(subStr, index):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""
    
    while counterChar < len(subStr):

        #New Weapon Type
        if subStr[counterChar:counterChar+17] == "export Descriptor" or counterChar == len(subStr)-1:
            if counterUnit > 0:

                OrderAvailability.append(copy.deepcopy(descriptor.order))

                for keyWord in range(len(OrderAvailability[index])):
                    OrderAvailability[index][keyWord] = [OrderAvailability[index][keyWord][0], analyze.variable(temporaryStr, OrderAvailability[index][keyWord])]

                index += 1

            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1


def extract(filePath):

    global OrderAvailability
    OrderAvailability = []
    
    extractOrderAvailability(open(filePath,"r").read(), 0)
    
    return OrderAvailability
