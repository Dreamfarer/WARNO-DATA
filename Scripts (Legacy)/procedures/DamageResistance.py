import copy
import helper.analyze

# Initialize gloabl variable
rootDirectory = None

def extractDamageResistance(subStr, index):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    rowString = "DamageTypeList;"

    TResistanceTypeRTTI = ["DamageTypeList"]
    TDamageTypeRTTI = []
    
    while counterChar < len(subStr):
        
        if subStr[counterChar:counterChar+19] == "TResistanceTypeRTTI" or subStr[counterChar:counterChar+15] == "TDamageTypeRTTI" or counterChar == len(subStr)-1:
            if counterUnit > 0:

                temporaryStr = helper.analyze.convertTypeRTTI(temporaryStr[:temporaryStr.find("\n", 0)-1])

                #Get ResistanceTypeList
                if temporaryStr[1] == "TResistanceTypeRTTI":
                    TResistanceTypeRTTI.append(temporaryStr[0])
                    rowString += temporaryStr[0] + ";"
                    
                #Get DamageTypeList
                else:
                    TDamageTypeRTTI.append(temporaryStr[0])
                
                index += 1
                
            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

    #Gather Values

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    rowString = rowString[:-1] + "\n"

    while counterChar < len(subStr):
        
        # Beginning of a new list of resistance values for the specifc damage type
        if subStr[counterChar:counterChar+1] == "[" or counterChar == len(subStr)-1:
            
            # Enter condition only after ResistanceTypeList and DamageTypeList has been passed (algorithm goes through whole file again)
            if counterUnit > 3:

                temporaryStr = temporaryStr[1:temporaryStr.find("]")-1]
                temporaryStr = temporaryStr.translate({ord(' '):None}) # Remove whitespaces
                temporaryStr = temporaryStr.translate({ord(','):ord(';')}) # Replace "," with ";"

                rowString += TDamageTypeRTTI[counterUnit-4] + ";" + temporaryStr + "\n"

            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

    return ["DamageResistance", TResistanceTypeRTTI, rowString]

def extract(filePath):

    #Return array with [column-names, data]
    return extractDamageResistance(open(rootDirectory + filePath,"r").read(), 0)
