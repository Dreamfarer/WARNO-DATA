## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT.
This project aims at understanding and interpreting these values for the ultimate goal: WARNO API
Feel free to contribute!

Following there is a list of varibles I've found so far:

## Unit Descriptor
All useful values to be found in `UniteDescriptor.ndf`

#### Unit Type
`String` **MotherCountry**\
`String` **AcknowUnitType**\
`String` **TypeUnitFormation**\
`String` **TypeUnitValue**\

#### Experience
* **ExperienceGainBySecond**
* **ExperienceMultiplierBonusOnKill**
* **CanWinExperience**

#### Visibility
* **UnitConcealmentBonus**
* **UnitIsStealth**

#### Armor
* **StunFreezesUnits**
* **MaxSuppressionDamages**
* **SuppressDamagesRegenRatio**
* **MaxStunDamages**
* **StunDamagesRegen**
* **ArmorDescriptorFront**
* **ArmorDescriptorSides**
* **ArmorDescriptorRear**
* **ArmorDescriptorTop**
* **MaxDamages**
* **MaxHPForHUD** &mdash; Function not known
* **AutoOrientation**

* **Dangerousness**

#### Movement
* **MaxSpeed**
* **VitesseCombat**
* **SpeedBonusOnRoad**
* **MaxAcceleration**
* **MaxDeceleration**
* **TempsDemiTour**
* **VehicleSubType**

#### Supply
* **SupplyCapacity**
* **SupplyPriority**

#### Fuel
* **FuelCapacity**
* **FuelMoveDuration**

#### Vision
* **OpticalStrength**
* **OpticalStrengthAltitude**
* **UnitDetectStealthUnit**

#### Scanner
* **IdentifyBaseProbability**
* **TimeBetweenEachIdentifyRoll**

#### Production
* **ProductionYear**
* **ProductionTime**
* **Resource_CommandPoints**
* **Resource_Tickets**

#### Label
* **IsSupply**
* **IsBuilding**
* **IsTransporter**
* **IsCommandementUnit**
* **IsPlane**
* **IsParachutist**
* **UnitName**

#### User Interface
* **NameToken**
* **RealRoadSpeed**
* **UpgradeFromUnit**

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`