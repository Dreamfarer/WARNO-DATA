#Test with Leopard 2A3 RFA

#Descriptor_Unit_Leopard_2A3_RFA
#WeaponDescriptor_Leopard_2A3_RFA

#Multiple Types:
#MotherCountry = 'RFA'
#Nationalite = ENationalite/Allied


#DONE
#ClassNameForDebug
#Nationalite
#MotherCountry
#UnitConcealmentBonus
#ArmorDescriptorFront
#ArmorDescriptorSides
#ArmorDescriptorRear
#ArmorDescriptorTop
#MaxDamages
#HitRollECM
#Dangerousness
#MaxSpeed
#SpeedBonusOnRoad
#MaxAcceleration
#MaxDeceleration
#TempsDemiTour
#FuelCapacity
#FuelMoveDuration
#PorteeVision
#OpticalStrength
#OpticalStrengthAltitude
#IdentifyBaseProbability
#TimeBetweenEachIdentifyRoll
#ProductionYear
#ProductionTime
#IsTransporter
#IsPlane
#UnitAttackValue
#UnitDefenseValue

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
