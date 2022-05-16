import UnitDescriptor
import WeaponDescriptor
import csv

version = 73022

#Export Array to CSV
csv.export(UnitDescriptor.extract("data/UniteDescriptor.ndf"), version)
csv.export(WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version)

#Create table command for MySQL Workbench
csv.table("bedartch_foxhole", "UniteDescriptor", UnitDescriptor.extract("data/UniteDescriptor.ndf"), version)
csv.table("bedartch_foxhole", "WeaponDescriptor", WeaponDescriptor.extract("data/WeaponDescriptor.ndf"), version)
