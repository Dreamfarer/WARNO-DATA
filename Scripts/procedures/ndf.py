import copy
import helper.analyze

def working(subString, keywords, newUnitIdentifier):

    counterUnit = 0 #Count units (Only used to filter out the first catch)
    unitBuffer = "" #This holds the string of one unit
    unitArray = [] #Temporary list that holds every recorded unit

    for characterIndex in range(len(subString)):

        #New Weapon Type
        if subString[characterIndex:characterIndex+len(newUnitIdentifier)] == newUnitIdentifier or characterIndex == len(subString)-1:

            #We loop through a unit at the beginning of a new one. Therefore, the first catch is useless.
            if counterUnit == 0:
                counterUnit += 1
                unitBuffer += subString[characterIndex] #Record unit string
                continue

            #Append the template defined in descriptor.py to this array
            unitArray.append(copy.deepcopy(keywords))

            #Loop through every keyword defined in descriptor.py
            for keyWord in range(len(unitArray[-1])):
                unitArray[-1][keyWord] = [unitArray[-1][keyWord][0], helper.analyze.variable(unitBuffer, unitArray[-1][keyWord])]


            unitBuffer = "" #Reset sting after one unit is finished
            
        unitBuffer += subString[characterIndex] #Record unit string

    return unitArray

def extract(filePath, keywords, newUnitIdentifier):
    
    return working(open(filePath,"r").read(), keywords, newUnitIdentifier)
