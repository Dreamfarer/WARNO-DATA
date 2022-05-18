import copy
import descriptor
import analyze

def extractWeaponDescriptor(subStr, level, index):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    while counterChar < len(subStr):
        match level:
            case 0: 
                if subStr[counterChar:counterChar+23] == "export WeaponDescriptor" or counterChar == len(subStr)-1:
                    if counterUnit > 0:

                        WeaponDescriptor.append(copy.deepcopy(descriptor.weapon)) #Add a template copy

                        WeaponDescriptor[index[0]][0] = [WeaponDescriptor[index[0]][0][0], WeaponDescriptor[index[0]][0][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][0])]
                        WeaponDescriptor[index[0]][1] = [WeaponDescriptor[index[0]][1][0], WeaponDescriptor[index[0]][1][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][1])]
                        WeaponDescriptor[index[0]][2] = [WeaponDescriptor[index[0]][2][0], WeaponDescriptor[index[0]][2][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][2])]
                        WeaponDescriptor[index[0]][3] = [WeaponDescriptor[index[0]][3][0], WeaponDescriptor[index[0]][3][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][3])]
                        extractWeaponDescriptor(temporaryStr, level + 1, index)
                        
                        for listIndex in range(len(WeaponDescriptor[index[0]])):
                            WeaponDescriptor[index[0]][listIndex] = [WeaponDescriptor[index[0]][listIndex][0], WeaponDescriptor[index[0]][listIndex][2]]
                        
                        index[1] = 1
                        index[0] += 1

                    temporaryStr = ""
                    counterUnit += 1
            case 1:
                if subStr[counterChar:counterChar+24] == "TTurretTwoAxisDescriptor" or subStr[counterChar:counterChar+21] == "TTurretWeaponDescriptor" or subStr[counterChar:counterChar+27] == "TTurretInfanterieDescriptor" or counterChar == len(subStr)-1:
                    if counterUnit > 0:
                        addToIndex = 4 if index[1] == 1 else 17 + 7 *(index[1] -2)
                        WeaponDescriptor[index[0]][0+addToIndex] = [WeaponDescriptor[index[0]][0+addToIndex][0], WeaponDescriptor[index[0]][0+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][0+addToIndex])]
                        WeaponDescriptor[index[0]][1+addToIndex] = [WeaponDescriptor[index[0]][1+addToIndex][0], WeaponDescriptor[index[0]][1+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][1+addToIndex])]
                        WeaponDescriptor[index[0]][2+addToIndex] = [WeaponDescriptor[index[0]][2+addToIndex][0], WeaponDescriptor[index[0]][2+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][2+addToIndex])]
                        WeaponDescriptor[index[0]][3+addToIndex] = [WeaponDescriptor[index[0]][3+addToIndex][0], WeaponDescriptor[index[0]][3+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][3+addToIndex])]
                        index[1] = index[1] + 1
                        extractWeaponDescriptor(temporaryStr, level + 1, index)
                        index[2] = 1

                    temporaryStr = ""
                    counterUnit += 1
            case 2:
                if subStr[counterChar:counterChar+24] == "TMountedWeaponDescriptor" or counterChar == len(subStr)-1:
                    if counterUnit > 0:
                        addToIndex = 4 if index[1] == 2 else 17 + 7 *(index[1] -3)
                        addToIndex = addToIndex + 3 * (index[2])
                        WeaponDescriptor[index[0]][1+addToIndex] = [WeaponDescriptor[index[0]][1+addToIndex][0], WeaponDescriptor[index[0]][1+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][1+addToIndex])]
                        WeaponDescriptor[index[0]][2+addToIndex] = [WeaponDescriptor[index[0]][2+addToIndex][0], WeaponDescriptor[index[0]][1+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][2+addToIndex])]
                        WeaponDescriptor[index[0]][3+addToIndex] = [WeaponDescriptor[index[0]][3+addToIndex][0], WeaponDescriptor[index[0]][1+addToIndex][1], analyze.variable(temporaryStr, WeaponDescriptor[index[0]][3+addToIndex])]
                        index[2] = index[2] + 1

                    temporaryStr = ""
                    counterUnit += 1

        temporaryStr += subStr[counterChar]
        counterChar += 1

def extract(filePath):
    
    global WeaponDescriptor
    WeaponDescriptor = []
    
    extractWeaponDescriptor(open(filePath,"r").read(), 0, [0, 1, 1])
    
    return WeaponDescriptor
    
