import copy
import descriptor
import analyze

def convertTypeRTTI(typeRTTI):

    family = typeRTTI[typeRTTI.find("Family")+8:typeRTTI.find(" ")-1]
    index = typeRTTI[typeRTTI.find("Index")+6:-1]

    return [family + "_" + index, typeRTTI[:typeRTTI.find("(")]]

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

                temporaryStr = convertTypeRTTI(temporaryStr[:temporaryStr.find("\n", 0)-1])

                #Get ResistanceTypeList
                if temporaryStr[1] == "TResistanceTypeRTTI":
                    TResistanceTypeRTTI.append(temporaryStr[0])
                    rowString+= temporaryStr[0] + ";"
                    
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
        
        if subStr[counterChar:counterChar+1] == "[" or counterChar == len(subStr)-1:
            if counterUnit > 3:

                temporaryStr = temporaryStr[1:temporaryStr.find("]")-1]
                temporaryStr = temporaryStr.translate({ord(' '):None})
                temporaryStr = temporaryStr.translate({ord(','):ord(';')})

                rowString += TDamageTypeRTTI[counterUnit-4] + ";" + temporaryStr + "\n"

            temporaryStr = ""   
            counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

    return ["DamageResistance", TResistanceTypeRTTI, rowString]

def extract(filePath):

    #Return array with [column-names, data]
    return extractDamageResistance(open(filePath,"r").read(), 0)
