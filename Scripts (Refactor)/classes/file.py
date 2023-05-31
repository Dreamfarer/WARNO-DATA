import os
from classes.descriptor import Descriptor


class File:
    """Represents one .ndf file"""

    def __init__(self, ndfType: Descriptor) -> None:
        self.__ndfType = ndfType
        self.__content = self.read()
        self.__descriptors = ndfType.extract(self.__content)

    # Read whole file into a string
    def read(self) -> str:
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "test-data", self.__ndfType.fileName
        )
        with open(file_path, "r") as file:
            return file.read()

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for descriptor in self.__descriptors:
            representation += str(descriptor) + "\n"
        return representation
