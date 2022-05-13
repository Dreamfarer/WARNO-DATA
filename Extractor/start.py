import UnitDescriptor
import WeaponDescriptor
import csv

#Export Array to CSV
print(csv.export(UnitDescriptor.extract("data/UniteDescriptor.ndf")))
print(csv.export(WeaponDescriptor.extract("data/WeaponDescriptor.ndf")))

#Create table command for MySQL Workbench
print(csv.table("bedartch_foxhole", "UniteDescriptor", UnitDescriptor.extract("data/UniteDescriptor.ndf")))
print(csv.table("bedartch_foxhole", "WeaponDescriptor", WeaponDescriptor.extract("data/WeaponDescriptor.ndf")))

input ("Press Enter to close...")
