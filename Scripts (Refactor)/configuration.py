from classes.descriptor import Descriptor
from classes.descriptor import SubDescriptor

"""
ach of the following objects represents a descriptor to be read from a .ndf file. However, please be aware that there are two different types of descriptors that can be instantiated:
- Descriptor: Top-level descriptors of each file, such as each weapon in "WeaponDescriptor.ndf."
- SubDescriptor: Descriptors inside top-level descriptors, such as turretTwoAxis descriptors inside the weapon descriptors of "WeaponDescriptor.ndf."

Please find the linkages between the descriptors below. Be aware that this structure represents a mixture of "Descriptor" and "SubDescriptor."
.
└── DivisionRules/
    ├── DeckDivisionDescriptor
    └── UnitDescriptor/
        ├── OrderAvailability
        ├── DamageResistance (Defend)
        └── WeaponDescriptor/
            ├── TurretDescriptor/
            │   └── TurretDescriptor/
            │       └── MountedWeaponDescriptor
            └── AmmunitionDescriptor/
                └── DamageResistance (Attack)
"""

mountedWeapon = SubDescriptor(
    regex=r"(TMountedWeaponDescriptor).*?\n\s+([\s\S]*?\))",
    variables=[
        ["Ammunition", "reference"],
        ["NbWeapons", "integer"],
        ["SalvoStockIndex", "integer"],
    ],
)

turretInfanterie = SubDescriptor(
    regex=r"(TTurretInfanterieDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    sub_descriptors=[mountedWeapon],
)

turretTwoAxis = SubDescriptor(
    regex=r"(TTurretTwoAxisDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    variables=[
        ["AngleRotationMax", "float"],
        ["AngleRotationMaxPitch", "float"],
        ["AngleRotationMinPitch", "float"],
        ["VitesseRotation", "float"],
        ["OutOfRangeTrackingDuration", "float"],
    ],
    sub_descriptors=[mountedWeapon],
)

turretUnit = SubDescriptor(
    regex=r"(TTurretUnitDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    variables=[
        ["AngleRotationMax", "float"],
        ["AngleRotationMaxPitch", "float"],
        ["AngleRotationMinPitch", "float"],
    ],
    sub_descriptors=[mountedWeapon],
)

turretBombardier = SubDescriptor(
    regex=r"(TTurretBombardierDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    variables=[
        ["FlyingAltitude", "meters"],
        ["FlyingSpeed", "meters"],
    ],
    sub_descriptors=[mountedWeapon],
)

weaponDescriptor = Descriptor(
    file_name="WeaponDescriptor.ndf",
    file_name_parent="UniteDescriptor.ndf",
    file_name_child=["Ammunition.ndf"],
    regex=r"export\s+(\w+)\s+is\s+TWeaponManagerModuleDescriptor\s*(([\s\S]*?)(\s+\)\n\s+\]\n\)))",
    variables=[
        ["HasMainSalvo", "bool"],
        ["Salves", "list"],
        ["SalvoIsMainSalvo", "list"],
        ["AlwaysOrientArmorTowardsThreat", "bool"],
    ],
    sub_descriptors=[turretInfanterie, turretTwoAxis, turretBombardier, turretUnit],
)
