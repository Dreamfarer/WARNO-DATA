import descriptor
import os

exportDirectory = ""

def getReference(keyword):
    if keyword == "UniteDescriptor":
        return descriptor.unit
    elif keyword == "WeaponDescriptor":
        return descriptor.weapon
    elif keyword == "Ammunition":
        return descriptor.ammo
    elif keyword == "DeckDescriptor":
        return descriptor.deck
    
def writeToFile(content, folder, name, version):

    folderPath = os.path.join(exportDirectory, str(version), folder)

    try:
        os.mkdir(folderPath) 
    except:
        folderPath += "\\" + name
    else:
        folderPath += "\\" + name
    
    file = open(folderPath, "w")
    file.write(content)

def table(inputArray, version, filename, database, tableName):
    
    createTableString = "CREATE TABLE `" + database + "`.`" + tableName + "` (\n  `id` INT NOT NULL AUTO_INCREMENT,\n"

    #DamageResistance is special
    if inputArray[0] == "DamageResistance":
        createTableString += "  `" + inputArray[1][0] + "` VARCHAR(255) NULL,\n"
        
        for index in range(len(inputArray[1][1:])):
            createTableString += "  `" + inputArray[1][index+1] + "` FLOAT(15) NULL,\n"

        createTableString += "  PRIMARY KEY (`id`))\nENGINE = InnoDB\nDEFAULT CHARACTER SET = utf8\nCOLLATE = utf8_bin;"
        writeToFile(createTableString, "mysql", "createTable_" + filename + ".txt", version)
        return

    referenceArray = getReference(inputArray[0][0][0])

    for index in range(len(referenceArray)):
        
        if referenceArray[index][2] == str:
            createTableString += "  `" + referenceArray[index][0] + "` VARCHAR(255) NULL,\n"
        elif referenceArray[index][2] == int:
            createTableString += "  `" + referenceArray[index][0] + "` INT(10) NULL,\n"
        elif referenceArray[index][2] == float:
            createTableString += "  `" + referenceArray[index][0] + "` FLOAT(15) NULL,\n"
        elif referenceArray[index][2] == bool:
            createTableString += "  `" + referenceArray[index][0] + "` TINYINT(1) NULL,\n"
        elif referenceArray[index][2] == list:
            createTableString += "  `" + referenceArray[index][0] + "` JSON NULL,\n"

    createTableString += "  PRIMARY KEY (`id`))\nENGINE = InnoDB\nDEFAULT CHARACTER SET = utf8\nCOLLATE = utf8_bin;"
    writeToFile(createTableString, "mysql", "createTable_" + filename + ".txt", version)
    
def export(inputArray, version, filename):
    
    #DamageResistance is special
    if inputArray[0] == "DamageResistance":
        writeToFile(inputArray[2], "csv", filename + ".csv", version)
        return inputArray

    outputRow = ""
    
    #Build first row
    for index in range(len(inputArray[0])):
        outputRow += inputArray[0][index][0] + ";"
    outputRow = outputRow[:-1] + "\n" # Cut the last "," away and add a line break

    referenceArray = getReference(inputArray[0][0][0])

    #Add data into it
    for index in range(len(inputArray)):
        for columns in range(len(inputArray[index])):

            #If anything contains ' " ', replace it with ' ' ' TO BE DONE!
            
            if inputArray[index][columns][1] in [int, str, float, list, bool, None]:
                outputRow += ";"
            elif referenceArray[columns][2] == str:
                outputRow += "\"" + str(inputArray[index][columns][1]) + "\";"
            elif referenceArray[columns][2] == list:
                for x in range(len(inputArray[index][columns][1])):
                    inputArray[index][columns][1][x] = inputArray[index][columns][1][x]
                outputRow += "\"" + str(inputArray[index][columns][1]) + "\";"
            else:
                outputRow += str(inputArray[index][columns][1]) + ";"

        outputRow = outputRow[:-1] + "\n"
        
    writeToFile(outputRow, "csv", filename + ".csv", version)

    return inputArray
