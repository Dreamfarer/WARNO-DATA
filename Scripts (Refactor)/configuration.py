from classes.descriptor import Descriptor

"""
Linkings between output files:

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

mountedWeapon = Descriptor(
    regex=r"(TMountedWeaponDescriptor).*?\n\s+([\s\S]*?\))",
    variables=[
        ["Ammunition", "reference"],
        ["NbWeapons", "integer"],
        ["SalvoStockIndex", "integer"],
    ],
)

turretInfanterie = Descriptor(
    regex=r"(TTurretInfanterieDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    sub_descriptors=[mountedWeapon],
)

turretTwoAxis = Descriptor(
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

turretUnit = Descriptor(
    regex=r"(TTurretUnitDescriptor).*?\n\s+([\s\S]*? \)[\s\S]*? \))",
    variables=[
        ["AngleRotationMax", "float"],
        ["AngleRotationMaxPitch", "float"],
        ["AngleRotationMinPitch", "float"],
    ],
    sub_descriptors=[mountedWeapon],
)

turretBombardier = Descriptor(
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
