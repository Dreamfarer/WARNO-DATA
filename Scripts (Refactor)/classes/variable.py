import re


class Variable:
    """Represents one variable in a .ndf file"""

    def __init__(self, name: str, var_type: str) -> None:
        self.__name = name
        self.__var_type = var_type
        self.__regEx = None
        self.__value = None
        self.buildRegEx()

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__var_type

    @property
    def value(self):
        return self.__value

    # Build RegEx dependent on variable type
    def buildRegEx(self) -> None:
        if self.__var_type in ["bool", "float", "integer"]:
            self.__regEx = rf"{self.__name}\s+=\s+(\S+)"
        elif self.__var_type == "reference":
            self.__regEx = rf"{self.__name}\s+=\s+~\/(\S+)"
        elif self.__var_type == "meters":
            self.__regEx = rf"{self.__name}\s+=\s+\(\((\d+)\)\s*\*\s*Metre\)"
        elif self.__var_type == "list":
            self.__regEx = rf"{self.__name}\s+=\s+\[(.*?)\]"
        else:
            raise ValueError("Invalid variable type!")

    # Extract variable from .ndf with RegEx (called from descriptor.py)
    def extractValue(self, raw_ndf: str) -> None:
        print(self.__var_type)
        print("Autsch")
        match = re.search(self.__regEx, raw_ndf, re.DOTALL)
        if match:
            if self.__var_type == "list":
                result = re.findall(r"(-?\d+|True|False)", match.group(1))
                self.__value = "[" + ",".join(result) + "]"
            else:
                self.__value = match.group(1)

    # Debug representation
    def __repr__(self) -> str:
        return f"{self.__name} = {self.__value}"
