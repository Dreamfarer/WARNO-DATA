file = open("WeaponDescriptor.ndf","r").read()

counter = 0
unitCounter = 0
stringVehicle = ""

weaponCounter = 0
weaponRecord = [0, 0]

while True:

    if file[counter:counter+24] == "TTurretTwoAxisDescriptor" or file[counter:counter+21] == "TTurretUnitDescriptor" or file[counter:counter+27] == "TTurretInfanterieDescriptor":
        weaponCounter += 1

    if file[counter:counter+27] == "MountedWeaponDescriptorList": #New vehicle entry
        if unitCounter > 0:
            if weaponCounter > weaponRecord[0]:
                weaponRecord[0] = weaponCounter
                weaponRecord[1] = counter
            weaponCounter = 0
            
        unitCounter += 1 #Vehicle counter

    stringVehicle += file[counter]
        
    counter += 1 #Count up loop

    if counter == len(file):
        break

print(weaponRecord)
input("Uh yes daddy...")
