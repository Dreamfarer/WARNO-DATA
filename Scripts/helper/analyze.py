####################################################################
# CONSTANTS
####################################################################
class Constant:
    def __init__(self):
        self.distance = None
        self.speed = None
        self.altitudeMax = None
        self.pitchSpeed = None
        self.altitudeMinForRoll = None
        self.minRollSpeedForRoll = None

    def initialize(self):

        # constant_Distance = file("data/GDConstantes.ndf", "MultiplicateurMetreRTSVersDistanceFeedbackTactique")
        self.distance = 1.0 / 2.83 # has moved into a c-header file, for the meantime, we will just hard-code it
        self.speed = file(rootDirectory + "/Scripts/data/GDConstantes.ndf", "MultiplicateurMetreRTSVersVitesseTactiquePourVehicule")
        self.altitudeMax = file(rootDirectory + "/Scripts/data/AirplaneConstantes.ndf", "MaxAltitude is") #Metre
        self.pitchSpeed = file(rootDirectory + "/Scripts/data/AirplaneConstantes.ndf", "MaxPitchSpeed is")
        self.altitudeMinForRoll = file(rootDirectory + "/Scripts/data/AirplaneConstantes.ndf", "MinAltitudeForRoll is") #Metre
        self.minRollSpeedForRoll = file(rootDirectory + "/Scripts/data/AirplaneConstantes.ndf", "MinRollSpeedForRoll is")

# Initialize gloabl variables
rootDirectory = None
constants = Constant()

# Convert
def convertTypeRTTI(typeRTTI):

    family = typeRTTI[typeRTTI.find("Family")+8:typeRTTI.find(" ")-1]
    index = typeRTTI[typeRTTI.find("Index")+6:-1]

    return [family + "_" + index, typeRTTI[:typeRTTI.find("(")]]

####################################################################
# Convert 0 to int, 0.0 to float and False to 1
####################################################################
def stringToType(string):

    #Boolean
    if string == "True":
        return 1
    elif string == "False":
        return 0

    #Must be either float or string
    if string.find(".") != -1:
        try:
            return float(string)
        except:
            return string
    try:
        return int(string)
    except:
        return string


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
# SEARCH KEYWORD IN GIVEN TEXT AND RETRIEVE ITS VALUE
####################################################################
def variable(text, keyword):
    index = text.find(keyword[1])

    # The presence of the keyword itself means this unit posesses this ability
    if keyword[0] in ["RevealInfluence"]:
        if index != -1:
            return 1
        else:
            return 0
    
    # Return 'None' if the keyword hasn't been found
    if index == -1:
        return None

    # If the variable is of type: TDamageTypeRTTI, for example: TDamageTypeRTTI(Family="artillerie" Index=1)
    if keyword[0] == "Arme":
        keywordlength = len(keyword[1])
        captured = text[index+keywordlength:text.find("\n", index+keywordlength)]
        captured = captured.strip()
        captured = captured[2:]
        return convertTypeRTTI(captured)[0]

    # Special case for 'PackList': We need to record everything inbetween its []
    # if keyword[0] in ["PackList"]:
    #    return captured[captured.find("[") + 1:captured.find("]") - 1]
        
    #Append all parsed strings that are array like to this list
    if keyword[0] in ["RoleList", "SpecialtiesList", "Salves", "SalvoIsMainSalvo", "TraitsToken", "AvailableTransportList", "NumberOfUnitInPackXPMultiplier", "Orders", "DivisionTags", "PackList"]:

        # Array like parsed strings
        keywordlength = len(keyword[1])
        captured = text[index+keywordlength:text.find("]", index+keywordlength)]
        captured = captured.translate({ord('='):None})
        captured = captured.translate({ord('['):None})
        captured = captured.translate({ord('\''):None})
        captured = captured.translate({ord('"'):None})
        captured = captured.translate({ord(' '):None})
        captured = captured.translate({ord('\n'):None})
        captured = captured.translate({ord('/'):None})
        captured = captured.translate({ord('~'):None})

        #Append all parsed strings that are array like to this list which ONLY contain one element
        if keyword[0] in ["RoleList"]:
            return stringToType(captured.translate({ord(','):None}))

        # Append all parsed strings that are array like to this list which appear in form of a 2D array: [(x,y),(x,y)]
        if keyword[0] in ["PackList"]:
            captureArrayString = ""
            captureArray = []
            captureTuple = []

            for i in range(len(captured)):

                # Start of new tuple
                if captured[i] == "(":
                    captureArrayString = ""

                # First element of tuple is finished
                elif captured[i] == "," and captured[i-1] != ")":

                    # Modify the Descriptor; at the moment it is the deck descriptor, but we need the unit descriptor
                    captureArrayString = "Descriptor_Unit_" + captureArrayString[captureArrayString.find("multi") + 6:]
                    
                    captureTuple.append(stringToType(captureArrayString))
                    captureArrayString = ""

                # End of current tuple
                elif captured[i] == ")":

                    # Second element of tuple is finished
                    captureTuple.append(stringToType(captureArrayString))
                    captureArrayString = ""

                    captureArray.append(captureTuple) # Add tuple to list
                    captureTuple = [] # Reset tuple

                else:
                    captureArrayString += captured[i]

            # Export list
            if captureArray == []:
                return None
            else:
                return captureArray

        # Seperates the elements by looking at "," when array is in form of: [x,y,z,a,b, etc.]
        captureArrayString = ""
        captureArray = []
        for i in range(len(captured)):
            
            if captured[i] == ",":
                captureArray.append(stringToType(captureArrayString))
                captureArrayString = ""
            elif i+1 == len(captured):
                captureArrayString += captured[i]
                captureArray.append(stringToType(captureArrayString))
                captureArrayString = ""
            else:
                captureArrayString += captured[i]

        if captureArray == []:
            return None
        else:
            return captureArray 

    # Trim string to only contain valuable information (it will cut away everything after the line break)
    keywordlength = len(keyword[1])
    captured = text[index+keywordlength:text.find("\n", index+keywordlength)]
    captured = captured.translate({ord('\''):None})
    captured = captured.translate({ord('='):None})
    captured = captured.translate({ord(','):None})
    captured = captured.translate({ord('('):None})
    captured = captured.translate({ord(')'):None})
    captured = captured.translate({ord('~'):None})
    captured = captured.translate({ord('/'):None})
    captured = captured.translate({ord('"'):None})
    captured = captured.strip()

    #If content is specific
    if captured == "nil":
        return None
    
     # If the variable we search has the keyword included, record the whole variable (e.g keyword: Descriptor_Deck_ and the variable is: ~/Descriptor_Deck_Division_US_82nd_Airborne_multi)
    if keyword[0] == "DeckDescriptor":
        return text[index:text.find("\n", index)-1]

    # Special case because there are two different 'WeaponDescriptor', we need to specify.
    if keyword[0] == "WeaponDescriptor" and keyword[1] == "WeaponDescriptor":
        return text[index:text.find("\n", index)]
    
    #If keyword is a constant and always the same
    match keyword[0]:
        case "AltitudeMax":
            return constants.altitudeMax * constants.distance
        case "PitchSpeed":
            return constants.pitchSpeed
        case "AltitudeMinForRoll":
            return constants.altitudeMinForRoll * constants.distance
        case "MinRollSpeedForRoll":
            return constants.minRollSpeedForRoll

    #SPEED: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["MaxSpeed","MaxAcceleration","MaxDeceleration", "UpwardSpeed", "Speed"]:
        return float(captured[:-8]) * constants.speed

    #DISTANCE: For every value that has "* Metre" in it, chop it away and multiply it by the corresponding constant.
    if keyword[0] in ["AltitudeMin","Altitude","AgilityRadius", "PorteeMaximale", "PorteeMinimale", "PorteeMaximaleTBA", "PorteeMinimaleTBA", "PorteeMaximaleHA", "PorteeMinimaleHA", "AltitudeAPorteeMaximale", "AltitudeAPorteeMinimale", "DispersionAtMaxRange", "DispersionAtMinRange", "RadiusSplashPhysicalDamages", "RadiusSplashSuppressDamages", "RayonPinned", "DistanceForSpeed", "DeploymentShift"]:
        return float(captured[:-8]) * constants.distance

    # Cases of type 'export Descriptor_Unit_AeroRifles_CMD_US is TEntityDescriptor' and we only want 'Descriptor_Unit_AeroRifles_CMD_US'
    if keyword[0] in ["WeaponDescriptor","UniteDescriptor","OrderAvailability", "Divisions", "Ammunition"]:
        return captured[:captured.find(" ")]

    # Cases of type 'Factory = EDefaultFactories/Infantry' and we only want 'Infantry'
    if keyword[0] in ["Factory","Nationalite"]:
        return captured[captured.find("/") + 1:]

    #Return value in it's correct type
    return stringToType(captured)
