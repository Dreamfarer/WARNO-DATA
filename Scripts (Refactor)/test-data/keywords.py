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
    ["Arme", "Arme", str],  # Special case, don't remove ""
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
