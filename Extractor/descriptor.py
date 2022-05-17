unit = [
    ["UniteDescriptor", "export", str],
    ["ClassNameForDebug", "ClassNameForDebug", str],
    ["Nationalite", "Nationalite", str],
    ["MotherCountry", "MotherCountry", str],
    ["UnitConcealmentBonus", "UnitConcealmentBonus", float],
    ["ArmorDescriptorFront", "ArmorDescriptorFront", str],
    ["ArmorDescriptorSides", "ArmorDescriptorSides", str],
    ["ArmorDescriptorRear", "ArmorDescriptorRear", str],
    ["ArmorDescriptorTop", "ArmorDescriptorTop", str],
    ["MaxDamages", "MaxDamages", float],
    ["HitRollECM", "HitRollECM", float],
    ["Dangerousness", "Dangerousness  =", float],
    ["NbSoldatInGroupeCombat", "NbSoldatInGroupeCombat  =", int],
    ["MaxSpeed","MaxSpeed", float], #Metre 
    ["RoadSpeed"," RoadSpeed", int],
    ["SpeedBonusOnRoad","SpeedBonusOnRoad", float],
    ["MaxAcceleration","MaxAcceleration", float], #Metre
    ["MaxDeceleration","MaxDeceleration", float], #Metre
    ["TempsDemiTour","TempsDemiTour", float],
    ["FuelCapacity","FuelCapacity", int],
    ["FuelMoveDuration","FuelMoveDuration", float],
    ["Autonomy","Autonomy", float],
    ["OpticalStrength","OpticalStrength", int],
    ["OpticalStrengthAltitude","OpticalStrengthAltitude", int],
    ["IdentifyBaseProbability","IdentifyBaseProbability", float],
    ["TimeBetweenEachIdentifyRoll","TimeBetweenEachIdentifyRoll", float],
    ["ProductionYear","ProductionYear", int],
    ["IsTransporter","IsTransporter", bool],
    ["IsPlane","IsPlane", bool],
    ["UnitAttackValue","UnitAttackValue", int],
    ["UnitDefenseValue","UnitDefenseValue", int],
    ["EvacuationTime","EvacuationTime", int],
    ["TravelDuration","TravelDuration", int],
    ["RoleList", "RoleList", str],
    ["SpecialtiesList", "SpecialtiesList", list],
    ["Factory", "Factory", str],
    ["Resource_CommandPoints", "Resource_CommandPoints", int],
    ["RevealInfluence", "TInfluenceScoutModuleDescriptor", bool],
    ["UpgradeFromUnit", "UpgradeFromUnit", str],
    ["SupplyCapacity", "SupplyCapacity", float],
    ["UnlockableOrders", "UnlockableOrders", str],
    ["WeaponDescriptor", "WeaponDescriptor", str],
    ["Altitude", " Altitude =", float], #Metre
    ["AltitudeMax", "AltitudeMax", float],
    ["AltitudeMin", "AltitudeMin", float], #Metre
    ["AltitudeMinForRoll", "AltitudeMinForRoll", float],
    ["MinRollSpeedForRoll", "MinRollSpeedForRoll", int],
    ["Speed", "Speed = (", float], #Metre
    ["AgilityRadius", "AgilityRadius", float], #Metre
    ["PitchAngle", "PitchAngle", int],
    ["RollAngle", "RollAngle", int],
    ["PitchSpeed", "PitchSpeed", float],
    ["RollSpeed", "RollSpeed =", int],
    ["UpwardSpeed", "UpwardSpeed", float], #Metre
    ["TorqueManoeuvrability", "TorqueManoeuvrability", int],
    ["CyclicManoeuvrability", "CyclicManoeuvrability", int],
    ["MaxInclination", "MaxInclination", int],
    ["GFactorLimit", "GFactorLimit", float],
    ["RotorArea", "RotorArea", int],
]

weapon = [
    ["WeaponDescriptor", "export", str], 
    ["Salves", "Salves", list], #Built like array
    ["HasMainSalvo", "HasMainSalvo", bool],
    ["SalvoIsMainSalvo", "SalvoIsMainSalvo", list], #Built like array
    ["Turret_1_AngleRotationMax", "AngleRotationMax", float],
    ["Turret_1_AngleRotationMaxPitch", "AngleRotationMaxPitch", float],
    ["Turret_1_AngleRotationMinPitch", "AngleRotationMinPitch", float],
    ["Turret_1_VitesseRotation", "VitesseRotation", float],
    ["Turret_1_Weapon_1_Ammunition", "Ammunition", str],
    ["Turret_1_Weapon_1_NbWeapons", "NbWeapons", int],
    ["Turret_1_Weapon_1_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_1_Weapon_2_Ammunition", "Ammunition", str],
    ["Turret_1_Weapon_2_NbWeapons", "NbWeapons", int],
    ["Turret_1_Weapon_2_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_1_Weapon_3_Ammunition", "Ammunition", str],
    ["Turret_1_Weapon_3_NbWeapons", "NbWeapons", int],
    ["Turret_1_Weapon_3_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_2_AngleRotationMax", "AngleRotationMax", float],
    ["Turret_2_AngleRotationMaxPitch", "AngleRotationMaxPitch", float],
    ["Turret_2_AngleRotationMinPitch", "AngleRotationMinPitch", float],
    ["Turret_2_VitesseRotation", "VitesseRotation", float],
    ["Turret_2_Weapon_1_Ammunition", "Ammunition", str],
    ["Turret_2_Weapon_1_NbWeapons", "NbWeapons", int],
    ["Turret_2_Weapon_1_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_3_AngleRotationMax", "AngleRotationMax", float],
    ["Turret_3_AngleRotationMaxPitch", "AngleRotationMaxPitch", float],
    ["Turret_3_AngleRotationMinPitch", "AngleRotationMinPitch", float],
    ["Turret_3_VitesseRotation", "VitesseRotation", float],
    ["Turret_3_Weapon_1_Ammunition", "Ammunition", str],
    ["Turret_3_Weapon_1_NbWeapons", "NbWeapons", int],
    ["Turret_3_Weapon_1_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_4_AngleRotationMax", "AngleRotationMax", float],
    ["Turret_4_AngleRotationMaxPitch", "AngleRotationMaxPitch", float],
    ["Turret_4_AngleRotationMinPitch", "AngleRotationMinPitch", float],
    ["Turret_4_VitesseRotation", "VitesseRotation", float],
    ["Turret_4_Weapon_1_Ammunition", "Ammunition", str],
    ["Turret_4_Weapon_1_NbWeapons", "NbWeapons", int],
    ["Turret_4_Weapon_1_SalvoStockIndex", "SalvoStockIndex", int],
    ["Turret_5_AngleRotationMax", "AngleRotationMax", float],
    ["Turret_5_AngleRotationMaxPitch", "AngleRotationMaxPitch", float],
    ["Turret_5_AngleRotationMinPitch", "AngleRotationMinPitch", float],
    ["Turret_5_VitesseRotation", "VitesseRotation", float],
    ["Turret_5_Weapon_1_Ammunition", "Ammunition", str],
    ["Turret_5_Weapon_1_NbWeapons", "NbWeapons", int],
    ["Turret_5_Weapon_1_SalvoStockIndex", "SalvoStockIndex", int]
]

ammo = [
    ["Ammunition", "export", str],
    ["Name", " Name ", str], #Enclosed in '
    ["TypeCategoryName", "TypeCategoryName", str], #Enclosed in '
    ["Caliber", "Caliber", str], #Enclosed in '
    ["TraitsToken", "TraitsToken", str], #Array enclosed in '
    ["Level", "Level", int],
    ["Arme", "Arme", str], #Special case, don't remove "" #NOT WORKING CORRECTLY
    ["Puissance", "Puissance", float],
    ["ShotsBeforeMaxNoise", "ShotsBeforeMaxNoise", int],
    ["NbTirParSalves", "NbTirParSalves", int],
    ["TempsEntreDeuxTirs", "TempsEntreDeuxTirs ", float],
    ["TempsEntreDeuxSalves", "TempsEntreDeuxSalves ", float],
    ["PorteeMaximale", " PorteeMaximale ", float], #Metre
    ["PorteeMinimale", " PorteeMinimale ", float], #Metre
    ["PorteeMaximaleTBA", "PorteeMaximaleTBA", float], #Metre
    ["PorteeMinimaleTBA", "PorteeMinimaleTBA", float], #Metre
    ["PorteeMaximaleHA", "PorteeMaximaleHA", float], #Metre
    ["PorteeMinimaleHA", "PorteeMinimaleHA", float], #Metre
    ["AltitudeAPorteeMaximale", "AltitudeAPorteeMaximale", float], #Metre
    ["AltitudeAPorteeMinimale", "AltitudeAPorteeMinimale", float], #Metre
    ["AffecteParNombre", "AffecteParNombre", bool],
    ["AngleDispersion", "AngleDispersion", float],
    ["DispersionAtMaxRange", "DispersionAtMaxRange", float], #Metre
    ["DispersionAtMinRange", "DispersionAtMinRange", float], #Metre
    ["RadiusSplashPhysicalDamages", "RadiusSplashPhysicalDamages", float], #Metre
    ["PhysicalDamages", " PhysicalDamages", float],
    ["RadiusSplashSuppressDamages", "RadiusSplashSuppressDamages", float], #Metre
    ["SuppressDamages", " SuppressDamages", float],
    ["RayonPinned", "RayonPinned", float], #Metre
    ["AllowSuppressDamageWhenNoImpact", "AllowSuppressDamageWhenNoImpact", bool],
    ["TirIndirect", "TirIndirect", bool],
    ["TirReflexe", "TirReflexe", bool],
    ["InterdireTirReflexe", "InterdireTirReflexe", bool],
    ["NoiseDissimulationMalus", "NoiseDissimulationMalus", float],
    ["BaseCriticModifier", "BaseCriticModifier", int],
    ["EBaseHitValueModifier_Idling", "EBaseHitValueModifier/Idling", int], #after ,
    ["EBaseHitValueModifier_Moving", "EBaseHitValueModifier/Moving", int], #after ,
    ["MaxSuccessiveHitCount", "MaxSuccessiveHitCount", int],
    ["TempsDeVisee", "TempsDeVisee", float],
    ["SupplyCost", "SupplyCost", int],
    ["CanShootOnPosition", "CanShootOnPosition", bool],
    ["CanShootWhileMoving", "CanShootWhileMoving", bool],
    ["NbrProjectilesSimultanes", "NbrProjectilesSimultanes", int],
    ["MissileDescriptor", "MissileDescriptor", str], #'Nil' if no descriptor
    ["SmokeDescriptor", "SmokeDescriptor", str], #'Nil' if no descriptor
    ["FireDescriptor", "FireDescriptor", str],
    ["CanHarmInfantry", "CanHarmInfantry", bool],
    ["CanHarmVehicles", "CanHarmVehicles", bool],
    ["CanHarmHelicopters", "CanHarmHelicopters", bool],
    ["CanHarmAirplanes", "CanHarmAirplanes", bool],
    ["CanHarmGuidedMissiles", "CanHarmGuidedMissiles", bool],
    ["IsHarmlessForAllies", "IsHarmlessForAllies", bool],
    ["PiercingWeapon", "PiercingWeapon", bool],
    ["DamageTypeEvolutionOverRangeDescriptor", "DamageTypeEvolutionOverRangeDescriptor", str], #'Nil' if no descriptor
    ["FlightTimeForSpeed", "FlightTimeForSpeed", float],
    ["DistanceForSpeed", "DistanceForSpeed", float] #Metre 
]
