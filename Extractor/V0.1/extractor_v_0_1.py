#Test with Leopard 2A3 RFA

#Descriptor_Unit_Leopard_2A3_RFA
#WeaponDescriptor_Leopard_2A3_RFA

#Multiple Types:
#MotherCountry = 'RFA'
#Nationalite = ENationalite/Allied

keyWordArray = [
    ["ClassNameForDebug", ""],
    ["Nationalite", ""],
    ["MotherCountry", ""],
    ["UnitConcealmentBonus", 0.0],
    ["ArmorDescriptorFront", ""],
    ["ArmorDescriptorSides", ""],
    ["ArmorDescriptorRear", ""],
    ["ArmorDescriptorTop", ""],
    ["MaxDamages", 0.0],
    ["HitRollECM", 0.0],
    ["Dangerousness", 0.0],
    ["MaxSpeed", 0],
    ["SpeedBonusOnRoad", 0.0],
    ["MaxAcceleration", 0.0],
    ["MaxDeceleration", 0.0],
    ["TempsDemiTour", 0.0],
    ["FuelCapacity", 0],
    ["FuelMoveDuration", 0],
    ["Autonomy", 0.0],
    ["OpticalStrength", 0],
    ["OpticalStrengthAltitude", 0],
    ["IdentifyBaseProbability", 0.0],
    ["TimeBetweenEachIdentifyRoll", 0.0],
    ["ProductionYear", 0],
    ["IsTransporter", False],
    ["IsPlane", False],
    ["UnitAttackValue", 0],
    ["UnitDefenseValue", 0],
]


#DONE

def analzye(text, keyword):
    index = text.find(keyword)
    keywordlength = len(keyword)
    captured = text[index+keywordlength:text.find("\n", index+keywordlength)]
    captured = captured.translate({ord('\''):None})
    captured = captured.translate({ord('='):None})
    captured = captured.strip()

    #Nationalite
    if keyword == "Nationalite":
        captured = captured[13:]
    
    return captured

file = open("UniteDescriptor.ndf","r").read()

counter = 0
unitCounter = 0
stringVehicle = ""
while True:

    stringVehicle += file[counter]
    
    #New vehicle entry
    if file[counter:counter+17] == "export Descriptor":
        if unitCounter > 0:
            
            #Do something with the data
            print(analzye(stringVehicle, "SuppressDamagesRegenRatio"))
            stringVehicle = ""
            
        unitCounter += 1 #Vehicle counter
        
    counter += 1 #Count up loop

    if counter == len(file):
        break



input("Press enter to continue...")
