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

## Ammunition Descriptor
All useful values to be found in `Ammunition.ndf`

`tkn` **Name**\
`tkn` **TypeCategoryName**\
`tkn` **Caliber**\
`str` **ProjectileType**\
`flt` **Puissance** &mdash; Function not known\
`flt` **TempsEntreDeuxTirs** &mdash; Time between two shots\
`int` **PorteeMinimale** &mdash; Maximal engagement distance (Ground)\
`int` **PorteeMaximale** &mdash; Minimal engagement distance (Ground)\
`int` **PorteeMinimaleTBA** &mdash; Maximal engagement distance (Helicopter)\
`int` **PorteeMaximaleTBA** &mdash; Minimal engagement distance (Helicopter)\
`int` **PorteeMinimaleHA** &mdash; Maximal engagement distance (Aircraft)\
`int` **PorteeMaximaleHA** &mdash; Minimal engagement distance (Aircraft)\
`int` **AltitudeAPorteeMaximale** &mdash; Maximal engagement altitude\
`int` **AltitudeAPorteeMinimale** &mdash; Minimal engagement altitude\
`int` **DispersionAtMaxRange** &mdash; Dispersion\
`flt` **CorrectedShotAimtimeMultiplier**\
`int` **RadiusSplashPhysicalDamages**\
`flt` **PhysicalDamages** &mdash; HE Damage\
`int` **RadiusSplashSuppressDamages**\
`flt` **SuppressDamages** &mdash; Suppress Damage\
`bol` **AllowSuppressDamageWhenNoImpact**\
`int` **EBaseHitValueModifier/Idling** &mdash; Accuracy while standing still\
`int` **EBaseHitValueModifier/Moving** &mdash; Accuracy while moving\
`flt` **TempsDeVisee** &mdash; Aim time\
`flt` **TempsEntreDeuxSalves** &mdash; Time between salvos\
`int` **NbTirParSalves** &mdash; Shot count per salvo\
`int` **SupplyCost**\
`flt` **FireTriggeringProbability**\
`bol` **CanShootOnPosition**\
`bol` **CanShootWhileMoving**\
`bol` **CanHarmInfantry**\
`bol` **CanHarmVehicles**\
`bol` **CanHarmHelicopters**\
`bol` **CanHarmAirplanes**\
`bol` **CanHarmGuidedMissiles**\
`bol` **IsHarmlessForAllies**\
`bol` **PiercingWeapon** &mdash; Function not known\