import copy
import keywords
import helper.analyze

def extractDivisionRules(subStr, level, deck):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    while counterChar < len(subStr):
        match level:
            case 0: 
                if subStr[counterChar:counterChar+16] == "Descriptor_Deck_" or counterChar == len(subStr)-1:
                    if counterUnit > 0:

                        extractDivisionRules(temporaryStr, level + 1, helper.analyze.variable(temporaryStr, keywords.deck[0]))

                    temporaryStr = ""
                    counterUnit += 1
            case 1:
                if subStr[counterChar:counterChar+14] == "TDeckUniteRule" or counterChar == len(subStr)-1:
                    if counterUnit > 0:

                        DivisionRules.append(copy.deepcopy(keywords.deck))
                        for listIndex in range(len(DivisionRules[-1])):
                            if listIndex == 0:
                                DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], deck] 
                            else:
                                DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], helper.analyze.variable(temporaryStr, DivisionRules[-1][listIndex])]

                    temporaryStr = ""
                    counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

def extract(filePath):
    
    global DivisionRules
    DivisionRules = []
    
    extractDivisionRules(open(filePath,"r").read(), 0, "")
    
    return DivisionRules
    
