## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT.
This project aims at understanding and interpreting these values for the ultimate goal: WARNO API
Feel free to contribute!

Following there is a list of varibles I've found so far:

## Useful Information
WARNO has some twists and turns when it comes down to comprehensibility. These are some useful tools to guide you through the jungle of WARNO data.

#### Constant Factors
Some values presented in `.ndf` files need to be multiplied by a constant factor. I know of **two** constants that are defined in `GDConstantes.ndf`:
* MultiplicateurMetreRTSVersDistanceFeedbackTactique: **1.0 div 2.83** &mdash; Needs to be multiplied with the *distance* to receive accurat results. E.g. 6000 \* (**1.0 / 2.83**)
* MultiplicateurMetreRTSVersVitesseTactiquePourVehicule: **0.45 div 1.0** &mdash; Needs to be multiplied with the *speed* to receive accurat results. E.g. 120 \* (**0.45 / 1.0**)

#### Calculate Road Speed
In `UniteDescriptor.ndf` there are values called *VitesseCombat* and *RealRoadSpeed* which are not being used. Instead, we should use *MaxSpeed*, which represents the off-road speed, and add *MaxSpeed* \* *SpeedBonusOnRoad* to get the true road speed. A huge thanks to WARNO modder *eMeM* for pointing this out to me over on Discord.

#### Armor-Piercing Damage (AP)
Currently, we do not understand how to retrieve the in-game displayed AP value. HE and suppress damage are no problems at all. What we currently believe:\
In `Ammunition.ndf` there is a value called *Arme* which references another file called `DamageResistance.ndf`. This file presents a table which holds all damage types in its rows and the damage dealt to every type of armor in its columns.

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
`str` **UpgradeFromUnit**

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`

`bol` **NeedsExplicitOrderToUseSmoke**\
`arr` **Salves** &mdash; Poorly understood\
`bol` **AlwaysOrientArmorTowardsThreat**\
`ref` **Ammunition** &mdash; References an object in `Ammunition.ndf`\
`flt` **OutOfRangeTrackingDuration** &mdash; Function not known

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
`int` **MaxSuccessiveHitCount**\
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