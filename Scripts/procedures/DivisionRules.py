import copy
import keywords
import helper.analyze
import procedures.ndf

# Initialize gloabl variable
rootDirectory = None

def extractDivisionRules(subStringDivisionRules, level, Divisions, divisionIndex):

    counterChar = 0
    counterUnit = 0
    temporaryStr = ""

    while counterChar < len(subStringDivisionRules):
        match level:
            case 0: 
                if subStringDivisionRules[counterChar:counterChar+16] == "Descriptor_Deck_" or counterChar == len(subStringDivisionRules)-1:
                    if counterUnit > 0:

                        # Iterate through the parsed data of 'Divisions.ndf' and find matches to 'DivisionRules.ndf'
                        for iteration in range(len(Divisions)):
                            if (Divisions[iteration][0][1] == helper.analyze.variable(temporaryStr, keywords.deck[0])):
                                divisionIndex = iteration

                        # Dig through this specific deck with recursion
                        extractDivisionRules(temporaryStr, level + 1, Divisions, divisionIndex)

                    temporaryStr = ""
                    counterUnit += 1
            case 1:
                if subStringDivisionRules[counterChar:counterChar+14] == "TDeckUniteRule" or counterChar == len(subStringDivisionRules)-1:
                    if counterUnit > 0:
                        
                        # Append copy of list structure from keywords.py
                        DivisionRules.append(copy.deepcopy(keywords.deck))

                        # Load 'Divisions.ndf' and cut out the relevant part

                        for listIndex in range(len(DivisionRules[-1])):

                            match listIndex:
                                case 0:
                                    # Add 'DeckDescriptor' which is the same for the whole deck
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 1:
                                    # Add 'DivisionName' which is the same for the whole deck (from Divisions.ndf)
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 2:
                                     # Add 'DivisionTags' which is the same for the whole deck (from Divisions.ndf)
                                     DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 3:
                                    # Add 'AvailableForPlay' which is the same for the whole deck (from Divisions.ndf)
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 4:
                                    # Add 'MaxActivationPoints' which is the same for the whole deck (from Divisions.ndf)
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 5:
                                    # Add 'CountryId' which is the same for the whole deck (from Divisions.ndf)
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][listIndex][1]] 
                                case 6:
                                    # Add 'UnitDescriptor'
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], helper.analyze.variable(temporaryStr, DivisionRules[-1][listIndex])]
                                case 7:
                                    # Add 'AvailableWithoutTransport'
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], helper.analyze.variable(temporaryStr, DivisionRules[-1][listIndex])]
                                case 8:
                                    # Add 'AvailableTransportList'
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], helper.analyze.variable(temporaryStr, DivisionRules[-1][listIndex])]
                                case 9:
                                    # Add 'MaxPackNumber' (This is very special: Search for DeckDescriptor + UnitDescriptor (without ~/Descriptor_Unit_) in Divisions.ndf and retrieve the number next to it)
                                    for iteration in range(len(Divisions[divisionIndex][6][1])):
                                        if Divisions[divisionIndex][6][1][iteration][0] == DivisionRules[-1][6][1]:
                                            DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], Divisions[divisionIndex][6][1][iteration][1]] 
                                            # print(Divisions[divisionIndex][6][1][iteration][1])
                                case 10:
                                    # Add 'NumberOfUnitInPack_Poor' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[0])
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], round(helper.analyze.variable(temporaryStr, ["NumberOfUnitInPack", "NumberOfUnitInPack ", int]) * helper.analyze.variable(temporaryStr, ["NumberOfUnitInPackXPMultiplier", "NumberOfUnitInPackXPMultiplier", list])[0])]
                                case 11:
                                    # Add 'NumberOfUnitInPack_Trained' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[1])
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], round(helper.analyze.variable(temporaryStr, ["NumberOfUnitInPack", "NumberOfUnitInPack ", int]) * helper.analyze.variable(temporaryStr, ["NumberOfUnitInPackXPMultiplier", "NumberOfUnitInPackXPMultiplier", list])[1])]
                                case 12:
                                    # Add 'NumberOfUnitInPack_Veteran' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[2])
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], round(helper.analyze.variable(temporaryStr, ["NumberOfUnitInPack", "NumberOfUnitInPack ", int]) * helper.analyze.variable(temporaryStr, ["NumberOfUnitInPackXPMultiplier", "NumberOfUnitInPackXPMultiplier", list])[2])]
                                case 13:
                                    # Add 'NumberOfUnitInPack_Elite' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[3])
                                    DivisionRules[-1][listIndex] = [DivisionRules[-1][listIndex][0], round(helper.analyze.variable(temporaryStr, ["NumberOfUnitInPack", "NumberOfUnitInPack ", int]) * helper.analyze.variable(temporaryStr, ["NumberOfUnitInPackXPMultiplier", "NumberOfUnitInPackXPMultiplier", list])[3])]

                                # 

                    temporaryStr = ""
                    counterUnit += 1

        temporaryStr += subStringDivisionRules[counterChar]
        counterChar += 1

def extract(filePathDivisionRules, filePathDivisions):
    
    global DivisionRules
    DivisionRules = []

    # Load relevant data from 'Divisions.ndf' first
    Divisions = procedures.ndf.extract(filePathDivisions, keywords.division, "export Descriptor")

    # Procede with 'DivisionRules.py'
    extractDivisionRules(open(rootDirectory + filePathDivisionRules,"r").read(), 0, Divisions, 0)
    
    return DivisionRules