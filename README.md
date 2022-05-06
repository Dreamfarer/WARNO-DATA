## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT. This project aims at understanding and interpreting these values for the ultimate goal: **WARNO API**\
Feel free to contribute! <3

## Useful Information
WARNO has some twists and turns when it comes down to comprehensibility. These are some useful tools to guide you through the jungle of WARNO data.

### Constant Factors
Some values presented in `.ndf` files need to be multiplied by a constant factor. I know of **two** constants so far that are defined in `GDConstantes.ndf`:
* MultiplicateurMetreRTSVersDistanceFeedbackTactique: **1.0 div 2.83** &mdash; Needs to be multiplied with the *distance* to receive accurat results. E.g. 6000 m \* (**1.0 / 2.83**) = 2120 m
* MultiplicateurMetreRTSVersVitesseTactiquePourVehicule: **0.45 div 1.0** &mdash; Needs to be multiplied with the *speed* to receive accurat results. E.g. 120 km/h \* (**0.45 / 1.0**) = 54 km/h

### Calculate Road Speed
In `UniteDescriptor.ndf` there are values called *VitesseCombat* and *RealRoadSpeed* which are not being used. Instead, we should use *MaxSpeed* which represents the off-road speed. Compute *MaxSpeed* \* constant_factor \* *SpeedBonusOnRoad* to get the true road speed.

### Armor-Piercing Damage (AP)
We need to distinguish between HE(AT) and Kinetic (KE). HE(AT) damage does **not** decrease with range, however, Kinetic (KE) does.\
Every ammunition type is defined in `Ammunition.ndf`. Firstly, we need to look in there at the *TraitsToken*, these will tell you if a weapon is Kinetic (KE) or not.

#### HE(AT)
If the ammunition type is not Kinetic (KE), the index of the variable *Arme* will be the AP damage value of the weapon (E.g. Arme = TDamageTypeRTTI(Family="ap" Index=11) will mean AP damage = 11).

#### Kinetic (KE)
The AP value of Kinetic (KE) ammunition **in-game** is given at the weapon's maximum range. In `Ammunition.ndf`, however, it is given at point-blank range. We need to calculate it first:\
AP_at_max_range = AP_at_point_blank - (max_range / range_factor)\
You might rightly ask yourself what value **range_factor** is: It is the amount of AP damage decrease over a given range. To find this value we need to look at to what **DamageTypeEvolutionOverRangeDescriptor** (`Ammunition.ndf`) is pointing to in `DamageStairTypeEvolutionOverRangeDescriptor`. E.g. *~/DamageTypeEvolutionOverRangeDescriptor_AP1_1Km* points to **Distance= 175.0, AP= 1.0** in `DamageStairTypeEvolutionOverRangeDescriptor`. This example will tell you that the AP damage decreases **1 point every 175m**.

#### Kinetic (KE) Calculation Example Leopard 2A3
We need to gather the information first:\
* AP_at_point_blank = Arme = TDamageTypeRTTI(Family="ap" Index=32) -> 32
* max_range = PorteeMaximale = ((6495) * Metre) -> 6495 \* (1.0 / 2.83) -> 2295 m
* range_factor = DamageTypeEvolutionOverRangeDescriptor = ~/DamageTypeEvolutionOverRangeDescriptor_AP1_1Km -> 175 m
Then we need to plug these values in the formula:\
**AP_at_max_range** = 32 - (2295 /  175) = **19**

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

## Special Thanks
I wanted to thank the following people. Whithout them, this project would have gone nowhere:
* **eMeM** over on Discord for the calculation of the road speed
* **unipus** over on Discord for pointing me in the right direction to understand AP damage for kinetic weapons

## Copyright Notice
Each and every bit of this data belongs to [Eugen Systems](https://eugensystems.com/). I soley dig through it to create a database for an WARNO API that will be accessible to the public for free.