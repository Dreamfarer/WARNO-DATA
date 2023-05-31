import re
from typing import List
from abc import ABC, abstractmethod
from classes.variable import Variable


class Descriptor(ABC):
    """This abstract class represents one descriptor in a .ndf file"""

    fileName = None
    descriptorPattern = None

    def __init__(self, name: str, content: str, variables: List["Variable"]) -> None:
        self.name = name
        self.content = content
        self.variables = variables
        for variable in self.variables:
            variable.getValue(self.content)

    # Extract whole descriptors from a given string
    @classmethod
    def extract(cls, content: str) -> List["Descriptor"]:
        descriptors = []
        matches = re.findall(cls.descriptorPattern, content, re.DOTALL)
        for match in matches:
            descriptors.append(cls(match[0], match[1]))
        return descriptors

    # Debug representation
    def __repr__(self) -> str:
        representation = f"\n{self.name}: "
        for variable in self.variables:
            representation += str(variable) + "\n"
        return representation
