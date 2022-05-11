unitDescriptor = [
    ["UniteDescriptor", "export",""], 
    ["ClassNameForDebug", "ClassNameForDebug",""],
    ["Nationalite", "Nationalite",""],
    ["MotherCountry", "MotherCountry", ""],
    ["UnitConcealmentBonus", "UnitConcealmentBonus", 0.0],
    ["ArmorDescriptorFront", "ArmorDescriptorFront",""],
    ["ArmorDescriptorSides", "ArmorDescriptorSides",""],
    ["ArmorDescriptorRear", "ArmorDescriptorRear", ""],
    ["ArmorDescriptorTop", "ArmorDescriptorTop", ""],
    ["MaxDamages", "MaxDamages",0.0],
    ["HitRollECM", "HitRollECM",0.0],
    ["Dangerousness", "Dangerousness  =",0.0],
    ["MaxSpeed","MaxSpeed", 0], #Metre
    ["RoadSpeed"," RoadSpeed", 0],
    ["SpeedBonusOnRoad","SpeedBonusOnRoad", 0.0],
    ["MaxAcceleration","MaxAcceleration", 0.0], #Metre
    ["MaxDeceleration","MaxDeceleration", 0.0], #Metre
    ["TempsDemiTour","TempsDemiTour", 0.0],
    ["FuelCapacity","FuelCapacity", 0],
    ["FuelMoveDuration","FuelMoveDuration", 0],
    ["Autonomy","Autonomy", 0.0],
    ["OpticalStrength","OpticalStrength", 0],
    ["OpticalStrengthAltitude","OpticalStrengthAltitude", 0],
    ["IdentifyBaseProbability","IdentifyBaseProbability", 0.0],
    ["TimeBetweenEachIdentifyRoll","TimeBetweenEachIdentifyRoll", 0.0],
    ["ProductionYear","ProductionYear", 0],
    ["IsTransporter","IsTransporter", False],
    ["IsPlane","IsPlane", False],
    ["UnitAttackValue","UnitAttackValue", 0],
    ["UnitDefenseValue","UnitDefenseValue", 0],
    ["EvacuationTime","EvacuationTime", 0],
    ["TravelDuration","TravelDuration", 0],
    ["RoleList", "RoleList", ""], #Built like array
    ["SpecialtiesList", "SpecialtiesList", []],
    ["Factory", "Factory", ""],
    ["Resource_CommandPoints", "Resource_CommandPoints", 0],
    ["UpgradeFromUnit", "UpgradeFromUnit", ""],
    ["SupplyCapacity", "SupplyCapacity", 0],
    ["UnlockableOrders", "UnlockableOrders", ""], #Reference to other file
    ["WeaponDescriptor", "WeaponDescriptor", ""],
    ["SupplyCapacity", "SupplyCapacity", 0.0],
    ["AltitudeMin", "AltitudeMin", 0.0], #Metre
    ["Altitude", " Altitude =", 0.0], #Metre
    ["AgilityRadius", "AgilityRadius", 0.0], #Metre
    ["PitchAngle", "PitchAngle", 0.0],
    ["RollAngle", "RollAngle", 0.0],
    ["RollSpeed", "RollSpeed =", 0.0],
    ["UpwardSpeed", "UpwardSpeed", 0.0], #Metre
    ["TorqueManoeuvrability", "TorqueManoeuvrability", 0.0],
    ["CyclicManoeuvrability", "CyclicManoeuvrability", 0.0],
    ["MaxInclination", "MaxInclination", 0.0],
    ["GFactorLimit", "GFactorLimit", 0.0],
    ["RotorArea", "RotorArea", 0.0],
    ["AltitudeMax", "AltitudeMax", 0.0],
    ["PitchSpeed", "PitchSpeed", 0.0],
    ["AltitudeMinForRoll", "AltitudeMinForRoll", 0.0],
    ["MinRollSpeedForRoll", "MinRollSpeedForRoll", 0.0],
]



####################################################################
# RETRIEVE A VARIABLE FROM A FILE
# filename: Name of the file the variable is defined in
# varName: Variable name
####################################################################
def getVariableFromNDFFile(filename, varName):

    #Read file into one large string
    file = open(filename,"r").read()

    #Capture variable
    index = file.find(varName)
    var = file[index+len(varName):file.find("\n", index+len(varName))]

    var = var.translate({ord('='):None})
    var = var.translate({ord('('):None})
    var = var.translate({ord(')'):None})
    
    if var.find("//") != -1:
        var = var[:var.find("//")]

    if var.find("* Metre") != -1:
        var = var[:var.find("* Metre")]
    
    var = var.strip()

    #Special Examples
    if varName == "MultiplicateurMetreRTSVersDistanceFeedbackTactique" or varName == "MultiplicateurMetreRTSVersVitesseTactiquePourVehicule":
        var1 = float(var[:var.find("div")])
        var2 = float(var[var.find("div")+3:])
        var = var1 / var2

    return var

####################################################################
# CONSTANTS
####################################################################
constant_Distance = getVariableFromNDFFile("GDConstantes.ndf", "MultiplicateurMetreRTSVersDistanceFeedbackTactique")
constant_Speed = getVariableFromNDFFile("GDConstantes.ndf", "MultiplicateurMetreRTSVersVitesseTactiquePourVehicule")
constant_AltitudeMax = getVariableFromNDFFile("AirplaneConstantes.ndf", "MaxAltitude is") #Metre
constant_PitchSpeed = getVariableFromNDFFile("AirplaneConstantes.ndf", "MaxPitchSpeed is")
constant_AltitudeMinForRoll = getVariableFromNDFFile("AirplaneConstantes.ndf", "MinAltitudeForRoll is") #Metre
constant_MinRollSpeedForRoll = getVariableFromNDFFile("AirplaneConstantes.ndf", "MinRollSpeedForRoll is")

####################################################################
# SEARCH KEYWORD IN GIVEN TEXT AND RETRIEVE ITS VALUE
####################################################################
def analzye(text, keyword):
    index = text.find(keyword[1])
    
    #If the given keyword does not exist
    if index == -1:
        return None
    
    #If keyword itself is present in the value 
    if keyword[0] == "WeaponDescriptor":
        keywordlength = len(keyword[1])
        captured = text[index:text.find("\n", index)]
        return captured

    #If value of keyword is NOT an array
    if keyword[0] != "RoleList" and keyword[0] != "SpecialtiesList" and keyword[0] != "Salves" and keyword[0] != "SalvoIsMainSalvo":
        keywordlength = len(keyword[1])
        captured = text[index+keywordlength:text.find("\n", index+keywordlength)]
        captured = captured.translate({ord('\''):None})
        captured = captured.translate({ord('='):None})
        captured = captured.translate({ord(','):None})
        captured = captured.translate({ord('('):None})
        captured = captured.translate({ord(')'):None})
        captured = captured.translate({ord('~'):None})
        captured = captured.translate({ord('/'):None})
        captured = captured.strip()
    else:
        keywordlength = len(keyword[1])
        captured = text[index+keywordlength:text.find("]", index+keywordlength)]
        captured = captured.translate({ord('='):None})
        captured = captured.translate({ord('['):None})
        captured = captured.translate({ord('\''):None})
        captured = captured.translate({ord(' '):None})
        captured = captured.translate({ord('\n'):None})

        #If array always has one element
        if keyword[0] != "SpecialtiesList" and keyword[0] != "Salves" and keyword[0] != "SalvoIsMainSalvo":
            return captured.translate({ord(','):None})

        #Seperate the elements by looking at ","
        captureArrayString = ""
        captureArray = []
        for i in range(len(captured)):
            if captured[i] == ",":
                captureArray.append(captureArrayString)
                captureArrayString = ""
            else:
                captureArrayString += captured[i]
                
        return captureArray #Returns array. Maybe it needs quotation marks to be a JSON array.

    #If keyword is a constant and always the same
    if keyword[0] == "AltitudeMax":
        return constant_AltitudeMax * constant_Distance
    if keyword[0] == "PitchSpeed":
        return constant_PitchSpeed
    if keyword[0] == "AltitudeMinForRoll":
        return constant_AltitudeMinForRoll * constant_Distance
    if keyword[0] == "MinRollSpeedForRoll":
        return constant_MinRollSpeedForRoll

    #If value is a Boolean, convert it to "1" and "0"
    if captured == "False":
        return 0
    if captured == "True":
        return 1

    #SPEED: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["MaxSpeed","MaxAcceleration","MaxDeceleration", "UpwardSpeed"]:
        return float(captured[:-8]) * constant_Speed

    #Distance: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["AltitudeMin","Altitude","AgilityRadius"]:
        return float(captured[:-8]) * constant_Distance

    #Special cases
    match keyword[0]:
        case "UniteDescriptor":
            return captured[:-21]
        case "Factory":
            return captured[17:]
        case "Nationalite":
            return captured[12:]

    #If keyword is a number
    if keyword[2] == 0.0:
        return float(captured)
    
    return captured

WeaponDescriptor = [
    ["Salves", "Salves", []], #Built like array
    ["HasMainSalvo", "HasMainSalvo", False],
    ["SalvoIsMainSalvo", "SalvoIsMainSalvo", []], #Built like array
    ["Turret_1_AngleRotationMax", "AngleRotationMax", None],
    ["Turret_1_AngleRotationMaxPitch", "AngleRotationMaxPitch", None],
    ["Turret_1_AngleRotationMinPitch", "AngleRotationMinPitch", None],
    ["Turret_1_VitesseRotation", "VitesseRotation", None],
    ["Turret_1_Weapon_1_Ammunition", "Ammunition", None],
    ["Turret_1_Weapon_1_NbWeapons", "NbWeapons", None],
    ["Turret_1_Weapon_1_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_1_Weapon_2_Ammunition", "Ammunition", None],
    ["Turret_1_Weapon_2_NbWeapons", "NbWeapons", None],
    ["Turret_1_Weapon_2_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_1_Weapon_3_Ammunition", "Ammunition", None],
    ["Turret_1_Weapon_3_NbWeapons", "NbWeapons", None],
    ["Turret_1_Weapon_3_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_2_AngleRotationMax", "AngleRotationMax", None],
    ["Turret_2_AngleRotationMaxPitch", "AngleRotationMaxPitch", None],
    ["Turret_2_AngleRotationMinPitch", "AngleRotationMinPitch", None],
    ["Turret_2_VitesseRotation", "VitesseRotation", None],
    ["Turret_2_Weapon_1_Ammunition", "Ammunition", None],
    ["Turret_2_Weapon_1_NbWeapons", "NbWeapons", None],
    ["Turret_2_Weapon_1_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_3_AngleRotationMax", "AngleRotationMax", None],
    ["Turret_3_AngleRotationMaxPitch", "AngleRotationMaxPitch", None],
    ["Turret_3_AngleRotationMinPitch", "AngleRotationMinPitch", None],
    ["Turret_3_VitesseRotation", "VitesseRotation", None],
    ["Turret_3_Weapon_1_Ammunition", "Ammunition", None],
    ["Turret_3_Weapon_1_NbWeapons", "NbWeapons", None],
    ["Turret_3_Weapon_1_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_4_AngleRotationMax", "AngleRotationMax", None],
    ["Turret_4_AngleRotationMaxPitch", "AngleRotationMaxPitch", None],
    ["Turret_4_AngleRotationMinPitch", "AngleRotationMinPitch", None],
    ["Turret_4_VitesseRotation", "VitesseRotation", None],
    ["Turret_4_Weapon_1_Ammunition", "Ammunition", None],
    ["Turret_4_Weapon_1_NbWeapons", "NbWeapons", None],
    ["Turret_4_Weapon_1_SalvoStockIndex", "SalvoStockIndex", None],
    ["Turret_5_AngleRotationMax", "AngleRotationMax", None],
    ["Turret_5_AngleRotationMaxPitch", "AngleRotationMaxPitch", None],
    ["Turret_5_AngleRotationMinPitch", "AngleRotationMinPitch", None],
    ["Turret_5_VitesseRotation", "VitesseRotation", None],
    ["Turret_5_Weapon_1_Ammunition", "Ammunition", None],
    ["Turret_5_Weapon_1_NbWeapons", "NbWeapons", None],
    ["Turret_5_Weapon_1_SalvoStockIndex", "SalvoStockIndex", None]
]

def captureWeaponDescriptor():
    file = open("WeaponDescriptor.ndf","r").read()

    weaponSystemCounter = 0
    weaponSystemString = ""
    weaponSystemNumber = 0

    #Loop over every vehicle
    while weaponSystemCounter < len(file):
        if file[weaponSystemCounter:weaponSystemCounter+23] == "export WeaponDescriptor" or weaponSystemCounter == len(file)-1:
            if weaponSystemNumber > 0:
                print(WeaponDescriptor[0][0] + ": " + str(analzye(weaponSystemString, WeaponDescriptor[0])))
                print(WeaponDescriptor[1][0] + ": " + str(analzye(weaponSystemString, WeaponDescriptor[1])))
                print(WeaponDescriptor[2][0] + ": " + str(analzye(weaponSystemString, WeaponDescriptor[2])))

                turretCounter = 0
                turretString = ""
                turretNumber = 0

                #Loop over every turret
                while turretCounter < len(weaponSystemString):
                    if weaponSystemString[turretCounter:turretCounter+24] == "TTurretTwoAxisDescriptor" or weaponSystemString[turretCounter:turretCounter+21] == "TTurretUnitDescriptor" or weaponSystemString[turretCounter:turretCounter+27] == "TTurretInfanterieDescriptor" or turretCounter == len(weaponSystemString)-1:
                        print("WHYNOW?")
                        if turretNumber > 0:

                            add = 0
                            if turretNumber == 1:
                                add = 3
                            elif turretNumber >= 2:
                                add = 16 + 7 *(turretNumber -2)

                            print(WeaponDescriptor[0+add][0] + ": " + str(analzye(turretString, WeaponDescriptor[0+add])))
                            print(WeaponDescriptor[1+add][0] + ": " + str(analzye(turretString, WeaponDescriptor[1+add])))
                            print(WeaponDescriptor[2+add][0] + ": " + str(analzye(turretString, WeaponDescriptor[2+add])))
                            print(WeaponDescriptor[2+add][0] + ": " + str(analzye(turretString, WeaponDescriptor[2+add])))
                            
                            weaponCounter = 0
                            weaponString = ""
                            weaponNumber = 0

                            #Loop over every weapon
                            while weaponCounter < len(turretString):
                                if weaponSystemString[turretCounter:turretCounter+24] == "TMountedWeaponDescriptor" or weaponCounter == len(turretString)-1:
                                    if weaponNumber > 0:
                                        
                                        add = 0
                                        if turretNumber == 1:
                                            add = 3
                                        elif turretNumber >= 2:
                                            add = 16 + 7 *(turretNumber -2)

                                        add = add + 4

                                        add = add + 3 * (weaponNumber-1)

                                        
                                        print(WeaponDescriptor[1+add][0] + ": " + str(analzye(weaponString, WeaponDescriptor[1+add])))
                                        print(WeaponDescriptor[2+add][0] + ": " + str(analzye(weaponString, WeaponDescriptor[2+add])))
                                        print(WeaponDescriptor[2+add][0] + ": " + str(analzye(weaponString, WeaponDescriptor[2+add])))

                                    weaponNumber += 1
                                    weaponString = "" #Reset for next loop
                                
                                weaponString += turretString[weaponCounter]
                                weaponCounter += 1

                        turretNumber += 1
                        turretString = ""#Reset for next loop

                    turretString += weaponSystemString[turretCounter]
                    turretCounter += 1

            weaponSystemNumber += 1
            weaponSystemString = "" #Reset for next loop

        weaponSystemString += file[weaponSystemCounter]
        weaponSystemCounter += 1
        

def captureUnitDescriptor():
    file = open("UniteDescriptor.ndf","r").read()

    counter = 0
    unitCounter = 0
    stringVehicle = ""
    
    while True:

        #New Weapon Type
        if file[counter:counter+17] == "export Descriptor": #We need to include the last entry!!!! Change this
            if unitCounter > 0:

                for x in unitDescriptor:
                    print(x[0] + ": " + str(analzye(stringVehicle, x)))
                    
                print("")

                stringVehicle = ""
                
            unitCounter += 1 #Vehicle counter

        stringVehicle += file[counter]
            
        counter += 1 #Count up loop

        if counter == len(file):
            break

captureWeaponDescriptor()
#captureUnitDescriptor()
input("Press enter to continue...")
