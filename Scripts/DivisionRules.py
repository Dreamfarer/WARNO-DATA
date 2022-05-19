import copy
import descriptor
import analyze

def extractDivisionRules(subStr, level):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    while counterChar < len(subStr):
        match level:
            case 0: 
                if subStr[counterChar:counterChar+16] == "Descriptor_Deck_" or counterChar == len(subStr)-1:
                    if counterUnit > 0:

                        #Record deck name

                        print("Bla")
                        
                        #WeaponDescriptor.append(copy.deepcopy(descriptor.weapon)) #Add a template copy

                        #WeaponDescriptor[index[0]][0] = [WeaponDescriptor[index[0]][0][0], WeaponDescriptor[index[0]][0][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][0])]
                        #WeaponDescriptor[index[0]][1] = [WeaponDescriptor[index[0]][1][0], WeaponDescriptor[index[0]][1][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][1])]
                        #WeaponDescriptor[index[0]][2] = [WeaponDescriptor[index[0]][2][0], WeaponDescriptor[index[0]][2][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][2])]
                        #WeaponDescriptor[index[0]][3] = [WeaponDescriptor[index[0]][3][0], WeaponDescriptor[index[0]][3][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][3])]
                        extractDivisionRules(temporaryStr, level + 1)
                        
                        #for listIndex in range(len(WeaponDescriptor[index[0]])):
                        #    WeaponDescriptor[index[0]][listIndex] = [WeaponDescriptor[index[0]][listIndex][0], WeaponDescriptor[index[0]][listIndex][2]]

                    temporaryStr = ""
                    counterUnit += 1
            case 1:
                if subStr[counterChar:counterChar+14] == "TDeckUniteRule" or counterChar == len(subStr)-1:
                    if counterUnit > 0:

                        #Record every other variable

                        DivisionRules.append(copy.deepcopy(descriptor.deck))

                        for listIndex in range(len(DivisionRules[-1])):
                            
                            print(analyze.variable(temporaryStr, DivisionRules[-1][listIndex]))
                        
                    temporaryStr = ""
                    counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

def extract(filePath):
    
    global DivisionRules
    DivisionRules = []
    
    extractDivisionRules(open(filePath,"r").read(), 0)
    
    return DivisionRules

extract("data/DivisionRules.ndf")
    
