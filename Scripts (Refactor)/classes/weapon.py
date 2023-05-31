from typing import List
from classes.variable import Variable
from classes.descriptor import Descriptor


class WeaponDescriptor(Descriptor):
    """This represents one weapon in WeaponDescriptor.ndf"""

    fileName = "WeaponDescriptor.ndf"
    descriptorPattern = r"export\s+(\w+)\s+is\s+TWeaponManagerModuleDescriptor\s*(([\s\S]*?)(\s+\)\n\s+\]\n\)))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())
        self.__turrets = []
        self.__turrets.extend(TurretInfanterieDescriptor.extract(content))
        self.__turrets.extend(TurretTwoAxisDescriptor.extract(content))
        self.__turrets.extend(TurretUnitDescriptor.extract(content))
        self.__turrets.extend(TurretBombardierDescriptor.extract(content))

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []
        variables.append(Variable("HasMainSalvo", "bool"))
        variables.append(Variable("Salves", "list"))
        variables.append(Variable("SalvoIsMainSalvo", "list"))
        variables.append(Variable("AlwaysOrientArmorTowardsThreat", "bool"))
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = f"\n\033[91m{self.name}:\033[0m\n"
        for variable in self.variables:
            representation += str(variable) + "\n"
        for turret in self.__turrets:
            if not turret == []:
                representation += "\nTurret:\n"
                representation += str(turret)
        return representation


class TurretInfanterieDescriptor(Descriptor):
    """This represents one turret from a weapon of WeaponDescriptor.ndf"""

    descriptorPattern = r"(TTurretInfanterieDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())
        self.__mountedWeapons = MountedWeaponDescriptor.extract(content)

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []  # Does not have variables
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for variable in self.variables:
            representation += "- " + str(variable) + "\n"
        for mountedWeapons in self.__mountedWeapons:
            representation += "- Mounted Weapon:\n"
            representation += str(mountedWeapons)
        return representation


class TurretTwoAxisDescriptor(Descriptor):
    """This represents one turret from a weapon of WeaponDescriptor.ndf"""

    descriptorPattern = r"(TTurretTwoAxisDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())
        self.__mountedWeapons = MountedWeaponDescriptor.extract(content)

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []
        variables.append(Variable("AngleRotationMax", "float"))
        variables.append(Variable("AngleRotationMaxPitch", "float"))
        variables.append(Variable("AngleRotationMinPitch", "float"))
        variables.append(Variable("VitesseRotation", "float"))
        variables.append(Variable("OutOfRangeTrackingDuration", "float"))
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for variable in self.variables:
            representation += "- " + str(variable) + "\n"
        for mountedWeapons in self.__mountedWeapons:
            representation += "- Mounted Weapon:\n"
            representation += str(mountedWeapons)
        return representation


class TurretUnitDescriptor(Descriptor):
    """This represents one turret from a weapon of WeaponDescriptor.ndf"""

    descriptorPattern = r"(TTurretUnitDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())
        self.__mountedWeapons = MountedWeaponDescriptor.extract(content)

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []
        variables.append(Variable("AngleRotationMax", "float"))
        variables.append(Variable("AngleRotationMaxPitch", "float"))
        variables.append(Variable("AngleRotationMinPitch", "float"))
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for variable in self.variables:
            representation += "- " + str(variable) + "\n"
        for mountedWeapons in self.__mountedWeapons:
            representation += "- Mounted Weapon:\n"
            representation += str(mountedWeapons)
        return representation


class TurretBombardierDescriptor(Descriptor):
    """This represents one turret from a weapon of WeaponDescriptor.ndf"""

    descriptorPattern = r"(TTurretBombardierDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())
        self.__mountedWeapons = MountedWeaponDescriptor.extract(content)

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []
        variables.append(Variable("FlyingAltitude", "meters"))
        variables.append(Variable("FlyingSpeed", "meters"))
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for variable in self.variables:
            representation += "- " + str(variable) + "\n"
        for mountedWeapons in self.__mountedWeapons:
            representation += "- Mounted Weapon:\n"
            representation += str(mountedWeapons)
        return representation


class MountedWeaponDescriptor(Descriptor):
    """This represents one mounted weapon of a turret from a weapon of WeaponDescriptor.ndf"""

    descriptorPattern = r"(TMountedWeaponDescriptor).*?\n\s+([\s\S]*?\))"

    def __init__(self, name: str, content: str) -> None:
        super().__init__(name, content, self.populate())

    # All variables that need to be read out for this descriptor
    def populate(self) -> List[Variable]:
        variables = []
        variables.append(Variable("Ammunition", "reference"))
        variables.append(Variable("NbWeapons", "integer"))
        variables.append(Variable("SalvoStockIndex", "integer"))
        return variables

    # Debug representation
    def __repr__(self) -> str:
        representation = ""
        for variable in self.variables:
            representation += "-- " + str(variable) + "\n"
        return representation
