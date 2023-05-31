import re


class Variable:
    """Represents one variable in a .ndf file"""

    def __init__(self, name: str, pattern: str) -> None:
        self.__name = name
        self.__pattern = pattern
        self.__value = None

    # Extract the value from within a descriptor that corresponds to the variable with self.__name
    # Each variable has a regex pattern dependent on it's type
    def getValue(self, content: str) -> None:
        if self.__pattern in ["bool", "float", "integer"]:
            regExp = rf"{self.__name}\s+=\s+(\S+)"
            match = re.search(regExp, content)
            if match:
                self.__value = match.group(1)

        elif self.__pattern == "list":
            regExp = rf"{self.__name}\s+=\s+\[(.*?)\]"
            match = re.search(regExp, content, re.DOTALL)
            if match:
                result = re.findall(r"(-?\d+|True|False)", match.group(1))
                self.__value = "[" + ",".join(result) + "]"

        elif self.__pattern == "reference":
            regExp = rf"{self.__name}\s+=\s+~\/(\S+)"
            match = re.search(regExp, content)
            if match:
                self.__value = match.group(1)

        elif self.__pattern == "meters":
            regExp = rf"{self.__name}\s+=\s+\(\((\d+)\)\s*\*\s*Metre\)"
            match = re.search(regExp, content)
            if match:
                self.__value = match.group(1)

    # Debug representation
    def __repr__(self) -> str:
        return f"{self.__name} = {self.__value}"
