import re
from typing import List
from classes.variable import Variable


class DescriptorMaster:
    """
    The actual non-template class for a descriptor in a .ndf file. This class should never be instantiated by the user themselves because the 'File' class initiates the process of creating objects based on the template 'Descriptor' class.
    """

    def __init__(
        self,
        file_name: str,
        variables: List[Variable],
        sub_descriptors: List["DescriptorMaster"],
        name: str,
        raw_ndf: str,
    ) -> None:
        self.__file_name = file_name
        self.__variables = variables
        self.__sub_descriptors = sub_descriptors
        self.__name = name
        self.__raw_ndf = raw_ndf
        for variable in self.__variables:
            variable.extractValue(self.__raw_ndf)
        return

    @property
    def file_name(self):
        return self.__file_name

    @property
    def variables(self):
        return self.__variables

    @property
    def sub_descriptors(self):
        return self.__sub_descriptors

    @property
    def name(self):
        return self.__name

    @classmethod
    def extract(cls, reference: "Descriptor", raw_ndf: str) -> List["DescriptorMaster"]:
        """
        Receive the full, raw .ndf file and extract all descriptors of 'reference' type.
        Please mind that this function receives the descriptor template defined by you in 'configuration.py'. However, it returns a list of non-template Descriptors that actually hold the data in the end.
        """
        descriptors = []
        matches = re.findall(reference.regex, raw_ndf, re.DOTALL)
        for match in matches:
            descriptors.append(
                cls(
                    reference.file_name,
                    cls.__create_variables(reference.variables),
                    cls.__extract_sub_descriptors(reference.sub_descriptors, match[1]),
                    match[0],
                    match[1],
                )
            )
        return descriptors

    def __extract_sub_descriptors(
        sub_descriptors: List["Descriptor"], raw_ndf: str
    ) -> List["Descriptor"]:
        """
        Recurively instanciate all nested descriptors within 'Descriptor'.
        """
        subdescriptors_extracted = []
        for subdescriptor in sub_descriptors:
            subdescriptors_extracted.extend(
                DescriptorMaster.extract(subdescriptor, raw_ndf)
            )
        return subdescriptors_extracted

    def __create_variables(variables_str: List[str]) -> List[Variable]:
        """
        Convert variable templates of the form ['variable_name', 'type'] into 'Variable' classes.
        """
        variables = []
        for variable in variables_str:
            variables.append(Variable(variable[0], variable[1]))
        return variables

    def __repr__(self) -> str:
        """
        Recursive string representation of the 'Descriptor' and its subdescriptors for debug purposes.
        """
        representation = f"\n{self.__name}:\n"
        for variable in self.__variables:
            representation += str(variable) + "\n"
        if not self.__sub_descriptors == None:
            for sub_descriptor in self.__sub_descriptors:
                representation += str(sub_descriptor)
        return representation

    def csv(self) -> str:
        return "Bla"


class Descriptor:
    """
    A descriptor in .ndf files defines the boundaries between two configurations, such as two vehicles.
    To convert a raw .ndf file to Python objects, instantiate a 'File' class with this descriptor. These objects can then be used to export data to .csv files or create SQL query templates.
    """

    def __init__(
        self,
        regex: str,
        file_name: str = None,
        file_name_parent: str = None,
        file_name_child: list[str] = [],
        variables: list[list[str]] = [],
        sub_descriptors: List["Descriptor"] = [],
    ) -> None:
        self.__regex = regex
        self.__file_name = file_name
        self.__file_name_parent = file_name_parent
        self.__file_name_child = file_name_child
        self.__variables = variables
        self.__sub_descriptors = sub_descriptors
        self.__checkFile()

    def __checkFile(self):
        """Check whether all three name-variables are set for the descriptor to represent a file."""
        if (
            self.__file_name == None
            or self.__file_name_parent == None
            or self.__file_name_child == []
        ):
            if not (
                self.__file_name == None
                and self.__file_name_parent == None
                and self.__file_name_child == []
            ):
                print(self.__file_name)
                print(self.__file_name_parent)
                print(self.__file_name_child)
                raise ValueError(
                    "For the descriptor to represent a file, all three names must be set in 'configuration.py' for this descriptor."
                )

    @property
    def regex(self):
        return self.__regex

    @property
    def file_name(self):
        return self.__file_name

    @property
    def file_name_parent(self):
        return self.__file_name_parent

    @property
    def file_name_child(self):
        return self.__file_name_child

    @property
    def variables(self):
        return self.__variables

    @property
    def sub_descriptors(self):
        return self.__sub_descriptors
