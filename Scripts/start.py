import UnitDescriptor
import WeaponDescriptor
import Ammunition
import DamageResistance
import DivisionRules
import csv
import os

version = 73022
csv.exportDirectory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data Exported")

#Export Array to .csv
UnitDescriptorArray = csv.export(UnitDescriptor.extract("data/UniteDescriptor.ndf"), version, "UniteDescriptor")
WeaponDescriptorArray = csv.export(WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version, "WeaponDescriptor")
AmmunitionArray = csv.export(Ammunition.extract("data/Ammunition.ndf"), version, "Ammunition")
DamageResistanceArray = csv.export(DamageResistance.extract("data/DamageResistance.ndf"), version, "DamageResistance")
DivisionRulesArray = csv.export(DivisionRules.extract("data/DivisionRules.ndf"), version, "DivisionRules")

#'CREATE TABLE' SQL queries for MySQL Workbench
csv.table(UnitDescriptorArray, version, "UniteDescriptor", "bedartch_warno", "UniteDescriptor")
csv.table(WeaponDescriptorArray, version, "WeaponDescriptor", "bedartch_warno", "WeaponDescriptor")
csv.table(AmmunitionArray, version, "Ammunition", "bedartch_warno", "Ammunition")
csv.table(DamageResistanceArray, version, "DamageResistance", "bedartch_warno", "DamageResistance")
csv.table(DivisionRulesArray, version, "DivisionRules", "bedartch_warno", "DivisionRules")
