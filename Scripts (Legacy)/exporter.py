# PROCEDURES folder
import procedures.WeaponDescriptor
import procedures.DamageResistance
import procedures.DivisionRules
import procedures.ndf

# HELPER folder
import helper.csv
import helper.analyze

# Same folder
import keywords

# Other Modules
import os

# Specify game version
version = 80721

# Calculate directories
helper.analyze.rootDirectory = os.path.dirname(os.path.dirname(__file__))
procedures.WeaponDescriptor.rootDirectory = os.path.dirname(os.path.dirname(__file__))
procedures.DamageResistance.rootDirectory = os.path.dirname(os.path.dirname(__file__))
procedures.DivisionRules.rootDirectory = os.path.dirname(os.path.dirname(__file__))
procedures.ndf.rootDirectory = os.path.dirname(os.path.dirname(__file__))
helper.csv.exportDirectory = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "Data Exported"
)

# Set things up
helper.analyze.constants.initialize()

# Export Array to .helper.csv
UnitDescriptorArray = helper.csv.export(
    procedures.ndf.extract(
        "/Scripts/data/UniteDescriptor.ndf", keywords.unit, "export Descriptor"
    ),
    version,
    "UniteDescriptor",
    keywords.unit,
)
WeaponDescriptorArray = helper.csv.export(
    procedures.WeaponDescriptor.extract("/Scripts/data/WeaponDescriptor.ndf"),
    version,
    "WeaponDescriptor",
    keywords.weapon,
)
AmmunitionArray = helper.csv.export(
    procedures.ndf.extract(
        "/Scripts/data/Ammunition.ndf", keywords.ammo, "export Ammo"
    ),
    version,
    "Ammunition",
    keywords.ammo,
)
DamageResistanceArray = helper.csv.export(
    procedures.DamageResistance.extract("/Scripts/data/DamageResistance.ndf"),
    version,
    "DamageResistance",
    "",
)
DivisionRulesArray = helper.csv.export(
    procedures.DivisionRules.extract(
        "/Scripts/data/DivisionRules.ndf", "/Scripts/data/Divisions.ndf"
    ),
    version,
    "DivisionRules",
    keywords.deck,
)
OrderAvailabilityArray = helper.csv.export(
    procedures.ndf.extract(
        "/Scripts/data/OrderAvailability_Tactic.ndf",
        keywords.order,
        "export Descriptor",
    ),
    version,
    "OrderAvailability",
    keywords.order,
)

# 'CREATE TABLE' SQL queries for MySQL Workbench
helper.csv.table(
    UnitDescriptorArray,
    version,
    "UniteDescriptor",
    "perytron_warno",
    "UniteDescriptor",
    keywords.unit,
)
helper.csv.table(
    WeaponDescriptorArray,
    version,
    "WeaponDescriptor",
    "perytron_warno",
    "WeaponDescriptor",
    keywords.weapon,
)
helper.csv.table(
    AmmunitionArray,
    version,
    "Ammunition",
    "perytron_warno",
    "Ammunition",
    keywords.ammo,
)
helper.csv.table(
    DamageResistanceArray,
    version,
    "DamageResistance",
    "perytron_warno",
    "DamageResistance",
    "",
)
helper.csv.table(
    DivisionRulesArray,
    version,
    "DivisionRules",
    "perytron_warno",
    "DivisionRules",
    keywords.deck,
)
helper.csv.table(
    OrderAvailabilityArray,
    version,
    "OrderAvailability",
    "perytron_warno",
    "OrderAvailability",
    keywords.order,
)
