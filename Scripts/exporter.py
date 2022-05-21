#PROCEDURES folder
import procedures.WeaponDescriptor
import procedures.DamageResistance
import procedures.DivisionRules
import procedures.ndf

#HELPER folder
import helper.csv

#Same folder
import keywords

#Other Modules
import os

version = 73022
helper.csv.exportDirectory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data Exported")

#Export Array to .helper.csv
UnitDescriptorArray = helper.csv.export(procedures.ndf.extract("data/UniteDescriptor.ndf", keywords.unit, "export Descriptor"), version, "UniteDescriptor", keywords.unit)
WeaponDescriptorArray = helper.csv.export(procedures.WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version, "WeaponDescriptor", keywords.weapon)
AmmunitionArray = helper.csv.export(procedures.ndf.extract("data/Ammunition.ndf", keywords.ammo, "export Ammo"), version, "Ammunition", keywords.ammo)
DamageResistanceArray = helper.csv.export(procedures.DamageResistance.extract("data/DamageResistance.ndf"), version, "DamageResistance", "")
DivisionRulesArray = helper.csv.export(procedures.DivisionRules.extract("data/DivisionRules.ndf"), version, "DivisionRules", keywords.deck)
OrderAvailabilityArray = helper.csv.export(procedures.ndf.extract("data/OrderAvailability_Tactic.ndf", keywords.order, "export Descriptor"), version, "OrderAvailability", keywords.order)

#'CREATE TABLE' SQL queries for MySQL Workbench
helper.csv.table(UnitDescriptorArray, version, "UniteDescriptor", "bedartch_warno", "UniteDescriptor", keywords.unit)
helper.csv.table(WeaponDescriptorArray, version, "WeaponDescriptor", "bedartch_warno", "WeaponDescriptor", keywords.weapon)
helper.csv.table(AmmunitionArray, version, "Ammunition", "bedartch_warno", "Ammunition", keywords.ammo)
helper.csv.table(DamageResistanceArray, version, "DamageResistance", "bedartch_warno", "DamageResistance", "")
helper.csv.table(DivisionRulesArray, version, "DivisionRules", "bedartch_warno", "DivisionRules", keywords.deck)
helper.csv.table(OrderAvailabilityArray, version, "OrderAvailability", "bedartch_warno", "OrderAvailability", keywords.order)
