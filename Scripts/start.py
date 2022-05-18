import UnitDescriptor
import WeaponDescriptor
import Ammunition
import csv
import DamageResistance
import os

version = 73022
csv.exportDirectory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data Exported")

#Export Array to CSV
csv.export(UnitDescriptor.extract("data/UniteDescriptor.ndf"), version)
csv.export(WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version)
csv.export(Ammunition.extract("data/Ammunition.ndf"), version)
csv.export(DamageResistance.extract("data/DamageResistance.ndf"), version)

#Create table command for MySQL Workbench
csv.table("bedartch_warno", "UniteDescriptor", UnitDescriptor.extract("data/UniteDescriptor.ndf"), version)
csv.table("bedartch_warno", "WeaponDescriptor", WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version)
csv.table("bedartch_warno", "Ammunition", Ammunition.extract("data/Ammunition.ndf"), version)
csv.table("bedartch_warno", "DamageResistance", DamageResistance.extract("data/DamageResistance.ndf"), version)
