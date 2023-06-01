import os
from classes.descriptor import Descriptor
from classes.descriptor import DescriptorMaster
from typing import List


class File:
    """Represents one .ndf file"""

    def __init__(self, reference: Descriptor) -> None:
        self.__reference = reference
        self.__content = self.read()
        self.__descriptors = DescriptorMaster.extract(self.__reference, self.__content)
        self.__csv = self.__build_csv()

    def __build_csv(self) -> str:
        # Check if nested: If yes, it means we need to pre/postfix the variables
        has_sub_descriptors = False
        for descriptor in self.__descriptors:
            if not descriptor.sub_descriptors == []:
                has_sub_descriptors = True
                break

        print(self.max_nested_descriptors(self.__descriptors))

        return

    def max_nested_descriptors(
        self,
        descriptors_test: list[Descriptor],
    ) -> list[int]:
        """
        Returns the max. descriptor count per sub-descriptor level. E.g. [6, 5, 2] means that there are 6 descriptors which hold at max. 5 sub-descriptors which in turn hold at max another 2 sub-descriptors.
        Used for the .csv export because variable number of elements are not possible in the table.
        """
        levels = []

        def recursive_discovery(descriptors, depth):
            count = 0
            for element in descriptors:
                count += 1
                if not element.sub_descriptors == []:
                    recursive_discovery(element.sub_descriptors, depth + 1)
                while len(levels) <= depth:
                    levels.append(0)
                if levels[depth] < count:
                    levels[depth] = count

        recursive_discovery(descriptors_test, 0)
        return levels

    def read(self) -> str:
        """Read whole file into a string"""
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "test-data", self.__reference.file_name
        )
        with open(file_path, "r") as file:
            return file.read()

    def __repr__(self) -> str:
        """String representation of this object for debug purposes."""
        representation = ""
        for descriptor in self.__descriptors:
            representation += str(descriptor) + "\n"
        return representation
