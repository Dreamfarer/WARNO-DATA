## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT.
This project aims at understanding and interpreting these values for the ultimate goal: WARNO API
Feel free to contribute!

Following there is a list of varibles I've found so far:

## Unit Descriptor
All useful values to be found in `UniteDescriptor.ndf`

#### Unit Type
`str` **MotherCountry**\
`str` **AcknowUnitType**\
`str` **TypeUnitFormation**\
`str` **TypeUnitValue**

#### Experience
`ref` **ExperienceGainBySecond**\
`ref` **ExperienceMultiplierBonusOnKill**\
`bol` **CanWinExperience**

#### Visibility
`flt` **UnitConcealmentBonus**\
`bol` **UnitIsStealth**

#### Armor
`bol` **StunFreezesUnits**\
`ref` **MaxSuppressionDamages**\
`ref` **SuppressDamagesRegenRatio**\
`ref` **MaxStunDamages**\
`ref` **StunDamagesRegen**\
`str` **ArmorDescriptorFront**\
`str` **ArmorDescriptorSides**\
`str` **ArmorDescriptorRear**\
`str` **ArmorDescriptorTop**\
`flt` **MaxDamages**\
`int` **MaxHPForHUD** &mdash; Function not known\
`bol` **AutoOrientation**

`flt` **Dangerousness**

#### Movement
`int` **MaxSpeed**\
`int` **VitesseCombat**\
`flt` **SpeedBonusOnRoad**\
`flt` **MaxAcceleration**\
`flt` **MaxDeceleration**\
`flt` **TempsDemiTour**\
`str` **VehicleSubType**

#### Supply
`flt` **SupplyCapacity**\
`int` **SupplyPriority**

#### Fuel
`int` **FuelCapacity**\
`flt` **FuelMoveDuration**

#### Vision
`int` **OpticalStrength**\
`int` **OpticalStrengthAltitude**\
`bol` **UnitDetectStealthUnit**

#### Scanner
`flt` **IdentifyBaseProbability**\
`flt` **TimeBetweenEachIdentifyRoll**

#### Production
`int` **ProductionYear**\
`int` **ProductionTime**\
`int` **Resource_CommandPoints**\
`int` **Resource_Tickets**

#### Label
`bol` **IsSupply**\
`bol` **IsBuilding**\
`bol` **IsTransporter**\
`bol` **IsCommandementUnit**\
`bol` **IsPlane**\
`bol` **IsParachutist**\
`str` **UnitName**

#### User Interface
`str` **NameToken**\
`int` **RealRoadSpeed**\
`str` **UpgradeFromUnit**

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`