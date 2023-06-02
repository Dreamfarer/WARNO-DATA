import re
from abc import ABC, abstractmethod
from typing import List
from typing import List, Union
from classes.variable import Variable


class DescriptorMaster:
    """
    The actual non-template class for a descriptor in a .ndf file.
    This class should never be instantiated by the user themselves because the 'File' class initiates the process of creating objects based on the template 'Descriptor' class.
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
    def extract(
        cls, reference: Union["Descriptor", "SubDescriptor"], raw_ndf: str
    ) -> List["DescriptorMaster"]:
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
        sub_descriptors: List["SubDescriptor"], raw_ndf: str
    ) -> List["SubDescriptor"]:
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


class DescriptorTemplate(ABC):
    """
    The template class for descriptors in .ndf files. Be aware that this class represents a template which is used to instantiate the data-holding "DescriptorMaster" automatically in a later step.
    This class should never be instantiated by the user themselves, rather use the "Descriptor" or "SubDescriptor" class.
    """

    def __init__(
        self,
        regex: str,
        file_name: str,
        file_name_parent: str,
        variables: list[list[str]] = [],
        sub_descriptors: List["SubDescriptor"] = [],
    ) -> None:
        self.__regex = regex
        self.__file_name = file_name
        self.__file_name_parent = file_name_parent
        self.__variables = variables
        self.__sub_descriptors = sub_descriptors

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


class Descriptor(DescriptorTemplate):
    """
    Represents a top-level descriptor to be read from a ".ndf" file. This class is used for descriptors that are directly contained within ".ndf" files, such as each weapon in the "WeaponDescriptor.ndf" file.

    To create instances of descriptors that are nested within top-level descriptors, use the "SubDescriptor" class.

    Attributes:
        regex (str): Regular expression pattern to extract this descriptor (create with https://regex101.com/)
        file_name (str): Name of to-be read .ndf file
        file_name_parent (str): Name of parent file which links to this file via an identifier variable
        reference_variable_parent (str): Name of variable in parent file that links to this descriptor
        variables (list[list[str]]): List that contains to-be read variables in from of ["variable_name", "type"]
        sub_descriptors (List["SubDescriptor"]): List that contains "SubDescriptor" objects, meaning non-top-level descriptors inside this descriptor.
    """

    def __init__(
        self,
        regex: str,
        file_name: str,
        file_name_parent: str,
        reference_variable_parent: str,
        variables: list[list[str]] = [],
        sub_descriptors: List["SubDescriptor"] = [],
    ) -> None:
        super().__init__(
            regex,
            file_name,
            file_name_parent,
            variables,
            sub_descriptors,
        )


class SubDescriptor(DescriptorTemplate):
    """
    Represents a non-top-level descriptor to be read from a ".ndf" file. This class is used for descriptors that are nested within top-level descriptors, such as the turrets of each weapon descriptor in the "WeaponDescriptor.ndf" file.

    To create instances of top-level descriptors, use the "Descriptor" class.

    Attributes:
        regex (str): Regular expression pattern to extract this descriptor (create with https://regex101.com/)
        variables (list[list[str]]): List that contains to-be read variables in from of ["variable_name", "type"]
        sub_descriptors (List["SubDescriptor"]): List that contains "SubDescriptor" objects, meaning non-top-level descriptors inside this descriptor.
    """

    def __init__(
        self,
        regex: str,
        variables: list[list[str]] = [],
        sub_descriptors: List["Descriptor"] = [],
    ) -> None:
        super().__init__(
            regex,
            None,
            None,
            variables,
            sub_descriptors,
        )
