#ADD PRIMARY KEY
#CREATE TABLE `bedartch_foxhole`.`WeaponDescriptor` (
#  `id` INT NOT NULL AUTO_INCREMENT,
#  `name` VARCHAR(255) NULL,
#  `weapondescriptor` VARCHAR(255) NOT NULL,
#  `WeaponDescriptorcol` TINYINT NULL,
#  `WeaponDescriptorcol1` JSON NULL,
#  PRIMARY KEY (`id`))
#ENGINE = InnoDB
#DEFAULT CHARACTER SET = utf8
#COLLATE = utf8_bin;

import descriptor

def table(database, tableName, inputArray):
    
    createTableString = "CREATE TABLE `" + database + "`.`" + tableName + "` (\n  `id` INT NOT NULL AUTO_INCREMENT,\n"

    referenceArray = []
    if inputArray[0][0][0] == "UniteDescriptor":
        referenceArray = descriptor.unit
    elif inputArray[0][0][0] == "WeaponDescriptor":
        referenceArray = descriptor.weapon

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

    return createTableString[:-2] + ")\nENGINE = InnoDB\nDEFAULT CHARACTER SET = utf8\nCOLLATE = utf8_bin;"
    
def export(inputArray):

    outputRow = ""
    
    #Build first row
    for index in range(len(inputArray[0])):
        outputRow += inputArray[0][index][0] + ";"
    outputRow = outputRow[:-1] + "\n" # Cut the last "," away and add a line break

    referenceArray = []
    if inputArray[0][0][0] == "UniteDescriptor":
        referenceArray = descriptor.unit
    elif inputArray[0][0][0] == "WeaponDescriptor":
        referenceArray = descriptor.weapon

    #Add data into it
    for index in range(len(inputArray)):
        for columns in range(len(inputArray[index])):

            if inputArray[index][columns][1] in [int, str, float, list, bool, None]:
                outputRow += ";"
            elif referenceArray[columns][2] == str:
                outputRow += "\"" + str(inputArray[index][columns][1]) + "\";"
            elif referenceArray[columns][2] == list:
                for x in range(len(inputArray[index][columns][1])):
                    inputArray[index][columns][1][x] = str(inputArray[index][columns][1][x])
                outputRow += "\"" + str(inputArray[index][columns][1]) + "\";"
            else:
                outputRow += str(inputArray[index][columns][1]) + ";"

        outputRow = outputRow[:-1] + "\n"

    return outputRow
