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
