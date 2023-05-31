# DEVELOPEMENT TO DO LIST
# Keywords mentioned here have not been implemented in the refactor
# However, this file has no use in the new version

unit = [
    ["UniteDescriptor", "export", str],
    [
        "ClassNameForDebug",
        "ClassNameForDebug",
        str,
    ],  # Only necessary until we are able to decode tokens
    ["Nationalite", "Nationalite", str],
    ["MotherCountry", "MotherCountry", str],
    ["UnitConcealmentBonus", "UnitConcealmentBonus", float],
    ["ArmorDescriptorFront", "ArmorDescriptorFront", str],
    ["ArmorDescriptorSides", "ArmorDescriptorSides", str],
    ["ArmorDescriptorRear", "ArmorDescriptorRear", str],
    ["ArmorDescriptorTop", "ArmorDescriptorTop", str],
    ["MaxDamages", "MaxDamages", float],
    ["HitRollECM", "HitRollECM", float],
    ["NbSoldatInGroupeCombat", "NbSoldatInGroupeCombat  =", int],
    ["MaxSpeed", "MaxSpeed", float],  # Metre
    ["RoadSpeed", " RoadSpeed", int],
    ["SpeedBonusOnRoad", "SpeedBonusOnRoad", float],
    ["MaxAcceleration", "MaxAcceleration", float],  # Metre
    ["MaxDeceleration", "MaxDeceleration", float],  # Metre
    ["TempsDemiTour", "TempsDemiTour", float],
    ["FuelCapacity", "FuelCapacity", int],
    ["FuelMoveDuration", "FuelMoveDuration", float],
    ["Autonomy", "Autonomy", float],
    ["OpticalStrength", "OpticalStrength", int],
    ["OpticalStrengthAltitude", "OpticalStrengthAltitude", int],
    ["IdentifyBaseProbability", "IdentifyBaseProbability", float],
    ["TimeBetweenEachIdentifyRoll", "TimeBetweenEachIdentifyRoll", float],
    ["TransportedSoldier", "TransportedSoldier", str],
    ["IsTowable", "IsTowable", bool],
    ["ProductionYear", "ProductionYear", int],
    ["UnitAttackValue", "UnitAttackValue", int],
    ["UnitDefenseValue", "UnitDefenseValue", int],
    ["EvacuationTime", "EvacuationTime", int],
    ["TravelDuration", "TravelDuration", int],
    ["RoleList", "RoleList", str],
    ["SpecialtiesList", "SpecialtiesList", list],
    ["Factory", "Factory", str],
    ["Resource_CommandPoints", "Resource_CommandPoints", int],
    ["Resource_Tickets", "Resource_Tickets", int],
    ["RevealInfluence", "TInfluenceScoutModuleDescriptor", bool],
    ["UpgradeFromUnit", "UpgradeFromUnit", str],
    ["SupplyCapacity", "SupplyCapacity", float],
    ["UnlockableOrders", "UnlockableOrders", str],
    ["WeaponDescriptor", "WeaponDescriptor", str],
    ["DeploymentShift", "DeploymentShift =", float],
    ["Altitude", " Altitude =", float],  # Metre
    ["AltitudeMax", "AltitudeMax", float],
    ["AltitudeMin", "AltitudeMin", float],  # Metre
    ["AltitudeMinForRoll", "AltitudeMinForRoll", float],
    ["MinRollSpeedForRoll", "MinRollSpeedForRoll", int],
    ["Speed", "Speed = (", float],  # Metre
    ["AgilityRadius", "AgilityRadius", float],  # Metre
    ["PitchAngle", "PitchAngle", int],
    ["RollAngle", "RollAngle", int],
    ["PitchSpeed", "PitchSpeed", float],
    ["RollSpeed", "RollSpeed =", int],
    ["UpwardSpeed", "UpwardSpeed", float],  # Metre
    ["TorqueManoeuvrability", "TorqueManoeuvrability", int],
    ["CyclicManoeuvrability", "CyclicManoeuvrability", int],
    ["MaxInclination", "MaxInclination", int],
    ["GFactorLimit", "GFactorLimit", float],
    ["RotorArea", "RotorArea", int],
]

ammo = [
    ["Ammunition", "export", str],
    ["Name", " Name ", str],  # Enclosed in '
    ["TypeCategoryName", "TypeCategoryName", str],  # Enclosed in '
    ["Caliber", "Caliber", str],  # Enclosed in '
    ["TraitsToken", "TraitsToken", str],  # Array enclosed in '
    ["Level", "Level", int],
    ["Arme", "Arme", str],  # Special case, don't remove ""
    ["Puissance", "Puissance", float],
    ["ShotsBeforeMaxNoise", "ShotsBeforeMaxNoise", int],
    ["NbTirParSalves", "NbTirParSalves", int],
    ["TempsEntreDeuxTirs", "TempsEntreDeuxTirs ", float],
    ["TempsEntreDeuxSalves", "TempsEntreDeuxSalves ", float],
    ["PorteeMaximale", " PorteeMaximale ", float],  # Metre
    ["PorteeMinimale", " PorteeMinimale ", float],  # Metre
    ["PorteeMaximaleTBA", "PorteeMaximaleTBA", float],  # Metre
    ["PorteeMinimaleTBA", "PorteeMinimaleTBA", float],  # Metre
    ["PorteeMaximaleHA", "PorteeMaximaleHA", float],  # Metre
    ["PorteeMinimaleHA", "PorteeMinimaleHA", float],  # Metre
    ["AltitudeAPorteeMaximale", "AltitudeAPorteeMaximale", float],  # Metre
    ["AltitudeAPorteeMinimale", "AltitudeAPorteeMinimale", float],  # Metre
    ["AffecteParNombre", "AffecteParNombre", bool],
    ["AngleDispersion", "AngleDispersion", float],
    ["DispersionAtMaxRange", "DispersionAtMaxRange", float],  # Metre
    ["DispersionAtMinRange", "DispersionAtMinRange", float],  # Metre
    ["DispersionWithoutSorting", "DispersionWithoutSorting", bool],
    ["RadiusSplashPhysicalDamages", "RadiusSplashPhysicalDamages", float],  # Metre
    ["PhysicalDamages", " PhysicalDamages", float],
    ["RadiusSplashSuppressDamages", "RadiusSplashSuppressDamages", float],  # Metre
    ["SuppressDamages", " SuppressDamages", float],
    ["RayonPinned", "RayonPinned", float],  # Metre
    ["AllowSuppressDamageWhenNoImpact", "AllowSuppressDamageWhenNoImpact", bool],
    ["TirIndirect", "TirIndirect", bool],
    ["TirReflexe", "TirReflexe", bool],
    ["InterdireTirReflexe", "InterdireTirReflexe", bool],
    ["NoiseDissimulationMalus", "NoiseDissimulationMalus", float],
    ["BaseCriticModifier", "BaseCriticModifier", int],
    ["EBaseHitValueModifier_Idling", "EBaseHitValueModifier/Idling", int],  # after ,
    ["EBaseHitValueModifier_Moving", "EBaseHitValueModifier/Moving", int],  # after ,
    ["MaxSuccessiveHitCount", "MaxSuccessiveHitCount", int],
    ["TempsDeVisee", "TempsDeVisee", float],
    ["SupplyCost", "SupplyCost", int],
    ["CanShootOnPosition", "CanShootOnPosition", bool],
    ["CanShootWhileMoving", "CanShootWhileMoving", bool],
    ["NbrProjectilesSimultanes", "NbrProjectilesSimultanes", int],
    ["MissileDescriptor", "MissileDescriptor", str],  #'Nil' if no descriptor
    ["SmokeDescriptor", "SmokeDescriptor", str],  #'Nil' if no descriptor
    ["FireDescriptor", "FireDescriptor", str],
    ["CanHarmInfantry", "CanHarmInfantry", bool],
    ["CanHarmVehicles", "CanHarmVehicles", bool],
    ["CanHarmHelicopters", "CanHarmHelicopters", bool],
    ["CanHarmAirplanes", "CanHarmAirplanes", bool],
    ["CanHarmGuidedMissiles", "CanHarmGuidedMissiles", bool],
    ["IsHarmlessForAllies", "IsHarmlessForAllies", bool],
    ["PiercingWeapon", "PiercingWeapon", bool],
    [
        "DamageTypeEvolutionOverRangeDescriptor",
        "DamageTypeEvolutionOverRangeDescriptor",
        str,
    ],  #'Nil' if no descriptor
    ["FlightTimeForSpeed", "FlightTimeForSpeed", float],
    ["DistanceForSpeed", "DistanceForSpeed", float],  # Metre
]

deck = [
    [
        "DeckDescriptor",
        "Descriptor_Deck_",
        str,
    ],  # Keyword itself is the variable, needs to be inserted into multiple rows
    ["DivisionName", "DivisionName ", str],  # Enclosed in '' (Divisions.ndf)
    ["DivisionTags", "DivisionTags ", list],  # Built like array (Divisions.ndf)
    ["AvailableForPlay", "AvailableForPlay ", bool],  # (Divisions.ndf)
    ["MaxActivationPoints", "MaxActivationPoints ", int],  # (Divisions.ndf)
    ["CountryId", "CountryId ", str],  # Enclosed in "" (Divisions.ndf)
    ["UnitDescriptor", "UnitDescriptor", str],  # OK
    ["AvailableWithoutTransport", "AvailableWithoutTransport", bool],  # OK
    ["AvailableTransportList", "AvailableTransportList", list],  # String Array #NOT
    [
        "MaxPackNumber",
        None,
        int,
    ],  # This is very special: Search for DeckDescriptor + UnitDescriptor (without ~/Descriptor_Unit_) in Divisions.ndf and retrieve the number next to it
    [
        "NumberOfUnitInPack_Poor",
        None,
        int,
    ],  #'NumberOfUnitInPack_Poor' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[0])
    [
        "NumberOfUnitInPack_Trained",
        None,
        int,
    ],  #'NumberOfUnitInPack_Trained' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[1])
    [
        "NumberOfUnitInPack_Veteran",
        None,
        int,
    ],  #'NumberOfUnitInPack_Veteran' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[2])
    [
        "NumberOfUnitInPack_Elite",
        None,
        int,
    ],  #'NumberOfUnitInPack_Elite' (NumberOfUnitInPack * NumberOfUnitInPackXPMultiplier[3])
]

division = [
    ["Divisions", "export", str],
    ["DivisionName", "DivisionName ", str],  # Enclosed in ''
    ["DivisionTags", "DivisionTags ", list],  # Built like array
    ["AvailableForPlay", "AvailableForPlay ", bool],
    ["MaxActivationPoints", "MaxActivationPoints ", int],
    ["CountryId", "CountryId ", str],  # Enclosed in ""
    ["PackList", "PackList ", list],  # 2d list in form of [unitName, availability]
]

order = [
    ["OrderAvailability", "export", str],  # Keyword itself is part of the vari
    ["Orders", " is ", list],  # OK
]
