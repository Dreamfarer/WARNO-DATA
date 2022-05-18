import helper

####################################################################
# RETRIEVE A VARIABLE FROM A readFile
# filename: Name of the readFile the variable is defined in
# varName: Variable name
####################################################################
def file(filename, varName):

    #Read readFile into one large string
    readFile = open(filename,"r").read()

    #Capture variable
    index = readFile.find(varName)
    var = readFile[index+len(varName):readFile.find("\n", index+len(varName))]

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

    return float(var)


####################################################################
# CONSTANTS
####################################################################
constant_Distance = file("data/GDConstantes.ndf", "MultiplicateurMetreRTSVersDistanceFeedbackTactique")
constant_Speed = file("data/GDConstantes.ndf", "MultiplicateurMetreRTSVersVitesseTactiquePourVehicule")
constant_AltitudeMax = file("data/AirplaneConstantes.ndf", "MaxAltitude is") #Metre
constant_PitchSpeed = file("data/AirplaneConstantes.ndf", "MaxPitchSpeed is")
constant_AltitudeMinForRoll = file("data/AirplaneConstantes.ndf", "MinAltitudeForRoll is") #Metre
constant_MinRollSpeedForRoll = file("data/AirplaneConstantes.ndf", "MinRollSpeedForRoll is")

####################################################################
# SEARCH KEYWORD IN GIVEN TEXT AND RETRIEVE ITS VALUE
####################################################################
def variable(text, keyword):
    index = text.find(keyword[1])

    #If descriptor itself is the variable
    if keyword[0] == "RevealInfluence":
        if index != -1:
            return 1
        else:
            return 0
    
    #If the given keyword does not exist
    if index == -1:
        return None

    #If keyword itself is present in the value 
    if keyword[0] == "WeaponDescriptor" and keyword[1] == "WeaponDescriptor":
        keywordlength = len(keyword[1])
        captured = text[index:text.find("\n", index)]
        return captured
    
    if keyword[0] == "Arme":
        keywordlength = len(keyword[1])
        captured = text[index+keywordlength:text.find("\n", index+keywordlength)]
        captured = captured.translate({ord('"'):ord('\'')})
        captured = captured.strip()
        return captured[1:]
        
    #If value of keyword is NOT an array
    if keyword[0] != "RoleList" and keyword[0] != "SpecialtiesList" and keyword[0] != "Salves" and keyword[0] != "SalvoIsMainSalvo" and keyword[0] != "TraitsToken":
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
        if keyword[0] != "SpecialtiesList" and keyword[0] != "Salves" and keyword[0] != "SalvoIsMainSalvo"and keyword[0] != "TraitsToken":
            return helper.stringToType(captured.translate({ord(','):None}))

        #Seperate the elements by looking at ","
        captureArrayString = ""
        captureArray = []
        for i in range(len(captured)):
            if captured[i] == ",": #We need a dedicated return type function which gives either integer, float, string or boolean back
                captureArray.append(helper.stringToType(captureArrayString))
                captureArrayString = ""
            else:
                captureArrayString += captured[i]
                
        return captureArray #Returns array. Maybe it needs quotation marks to be a JSON array.

    #If content is specific
    if captured == "nil":
        return None
    
    #If keyword is a constant and always the same
    if keyword[0] == "AltitudeMax":
        return constant_AltitudeMax * constant_Distance
    if keyword[0] == "PitchSpeed":
        return constant_PitchSpeed
    if keyword[0] == "AltitudeMinForRoll":
        return constant_AltitudeMinForRoll * constant_Distance
    if keyword[0] == "MinRollSpeedForRoll":
        return constant_MinRollSpeedForRoll

    #SPEED: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["MaxSpeed","MaxAcceleration","MaxDeceleration", "UpwardSpeed", "Speed"]:
        return float(captured[:-8]) * constant_Speed

    #Distance: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["AltitudeMin","Altitude","AgilityRadius", "PorteeMaximale", "PorteeMinimale", "PorteeMaximaleTBA", "PorteeMinimaleTBA", "PorteeMaximaleHA", "PorteeMinimaleHA", "AltitudeAPorteeMaximale", "AltitudeAPorteeMinimale", "DispersionAtMaxRange", "DispersionAtMinRange", "RadiusSplashPhysicalDamages", "RadiusSplashSuppressDamages", "RayonPinned", "DistanceForSpeed"]:
        return float(captured[:-8]) * constant_Distance

    #Special cases
    match keyword[0]:
        case "Ammunition":
            return captured[:-25]
        case "WeaponDescriptor":
            return captured[:-34]
        case "UniteDescriptor":
            return captured[:-21]
        case "Factory":
            return captured[17:]
        case "Nationalite":
            return captured[12:]

    #Return value in it's correct type
    return helper.stringToType(captured)
