from classes.descriptor import Descriptor
from classes.descriptor import SubDescriptor

"""
Each of the following objects represents a descriptor to be read from a .ndf file. However, please be aware that there are two different types of descriptors that can be instantiated:
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
    reference_variable_parent="WeaponManager",
    regex=r"export\s+(\w+)\s+is\s+TWeaponManagerModuleDescriptor\s*(([\s\S]*?)(\s+\)\n\s+\]\n\)))",
    variables=[
        ["HasMainSalvo", "bool"],
        ["Salves", "list"],
        ["SalvoIsMainSalvo", "list"],
        ["AlwaysOrientArmorTowardsThreat", "bool"],
    ],
    sub_descriptors=[turretInfanterie, turretTwoAxis, turretBombardier, turretUnit],
)

"""
Special variables:
- "Arme"

Removed since last time:
- Puissance
- RayonPinned
- CanHarmInfantry
- CanHarmVehicles
- CanHarmHelicopters
- CanHarmGuidedMissiles

Added since last time:
- ShowDamageInUI
"""
ammunitionDescriptor = Descriptor(
    file_name="Ammunition.ndf",
    file_name_parent="WeaponDescriptor.ndf",
    reference_variable_parent="Ammunition",
    regex=r"(Ammo_\w+)\s*is\s*TAmmunitionDescriptor\s*(\([\s\S]*?\n\))",
    variables=[
        ["Name", "string"],
        ["TypeCategoryName", "string"],
        ["Caliber", "string"],
        ["TraitsToken", "list"],
        ["Level", "integer"],
        ["ShotsBeforeMaxNoise", "integer"],
        ["NbTirParSalves", "integer"],
        ["TempsEntreDeuxTirs", "float"],
        ["TempsEntreDeuxSalves", "float"],
        ["PorteeMaximale", "meters"],
        ["PorteeMinimale", "meters"],
        ["PorteeMaximaleTBA", "meters"],
        ["PorteeMinimaleTBA", "meters"],
        ["PorteeMaximaleHA", "meters"],
        ["PorteeMinimaleHA", "meters"],
        ["AltitudeAPorteeMaximale", "meters"],
        ["AltitudeAPorteeMinimale", "meters"],
        ["AffecteParNombre", "bool"],
        ["AngleDispersion", "float"],
        ["DispersionAtMaxRange", "meters"],
        ["DispersionAtMinRange", "meters"],
        ["DispersionWithoutSorting", "bool"],
        ["RadiusSplashPhysicalDamages", "meters"],
        ["PhysicalDamages", "float"],
        ["RadiusSplashSuppressDamages", "meters"],
        ["SuppressDamages", "float"],
        ["AllowSuppressDamageWhenNoImpact", "bool"],
        ["TirIndirect", "bool"],
        ["TirReflexe", "bool"],
        ["InterdireTirReflexe", "bool"],
        ["NoiseDissimulationMalus", "float"],
        ["BaseCriticModifier", "integer"],
        ["EBaseHitValueModifier/Idling", "integer"],
        ["EBaseHitValueModifier/Moving", "integer"],
        ["MaxSuccessiveHitCount", "integer"],
        ["TempsDeVisee", "float"],
        ["SupplyCost", "integer"],
        ["CanShootOnPosition", "bool"],
        ["CanShootWhileMoving", "bool"],
        ["NbrProjectilesSimultanes", "integer"],
        ["MissileDescriptor", "reference"],
        ["SmokeDescriptor", "reference"],
        ["FireDescriptor", "reference"],
        ["CanHarmAirplanes", "bool"],
        ["IsHarmlessForAllies", "bool"],
        ["PiercingWeapon", "bool"],
        ["DamageTypeEvolutionOverRangeDescriptor", "reference"],
        ["FlightTimeForSpeed", "float"],
        ["DistanceForSpeed", "meters"],
    ],
    sub_descriptors=[turretInfanterie, turretTwoAxis, turretBombardier, turretUnit],
)
