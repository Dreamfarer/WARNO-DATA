## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT. This project aims at understanding and interpreting these values for the ultimate goal: **WARNO API**

## Useful Information
WARNO has some twists and turns when it comes down to comprehensibility. These are some useful tools to guide you through the jungle of WARNO data.

### Constant Factors
Some values presented in `.ndf` files need to be multiplied by a constant factor. I know of **two** constants so far that are defined in `GDConstantes.ndf`:
* MultiplicateurMetreRTSVersDistanceFeedbackTactique: **1.0 div 2.83** &mdash; Needs to be multiplied with the *distance* to receive accurate results. E.g. 6000 m \* (**1.0 / 2.83**) = 2120 m
* MultiplicateurMetreRTSVersVitesseTactiquePourVehicule: **0.45 div 1.0** &mdash; Needs to be multiplied with the *speed* to receive accurate results. E.g. 120 km/h \* (**0.45 / 1.0**) = 54 km/h

### Calculate Road Speed
In `UniteDescriptor.ndf` there are values called *VitesseCombat* and *RealRoadSpeed* which are not being used. Instead, we should use *MaxSpeed* which represents the off-road speed. Compute *MaxSpeed* \* constant_factor \* *SpeedBonusOnRoad* to get the true road speed.

### Armor-Piercing (AP) Damage
We need to distinguish between HE(AT) and Kinetic (KE). HE(AT) damage does **not** decrease with range, however, Kinetic (KE) does.\
Every ammunition type is defined in `Ammunition.ndf`. If \[Kinetic\] is listed in the *TraitsToken*-array, it means that this ammunition type is kinetic. If there is no such tag, the ammunition type is HE(AT).

#### HE(AT)
If the ammunition type is not Kinetic (KE), the index of the variable *Arme* will be the AP damage value of the weapon (E.g. Arme = TDamageTypeRTTI(Family="ap" Index=11) will mean an AP damage of 11).

#### Kinetic (KE)
The AP value of Kinetic (KE) ammunition **in-game** is given at the weapon's maximum range. In `Ammunition.ndf`, however, it is given at point-blank range. Therefore, we need to calculate it first:

*AP_max_range = AP_point_blank - (max_range / range_factor)*

* *AP_max_range*: AP damage at maximum range.
* *AP_point_blank*: AP damage at point-blank equivalent to the index defined in **Arme**.
* *max_range*: Maximal range defined in **PorteeMaximale**, multiplied with the corresponding constant factor.
* *range_factor*: Defined as the amount of AP damage decrease over a given range. To find this value we need to look at to what **DamageTypeEvolutionOverRangeDescriptor** is pointing to in `DamageStairTypeEvolutionOverRangeDescriptor.ndf`.\
E.g. *~/DamageTypeEvolutionOverRangeDescriptor_AP1_1Km* points to **Distance= 175.0, AP= 1.0**. In this case the AP damage decreases **1 point every 175m**.

### Experience & Veterancy
What experience scheme is currently being used can be seen under *ExperienceLevelsPackDescriptor* in `UniteDescriptor.ndf`. This string is a reference to `ExperienceLevels.ndf` where all schemes are defined. However, at the moment every unit uses the following experience scheme:
* *Level 0 (POOR)*: Time in-between salves = *115%*, Precision = *-25*, Suppress Damage = *125%*
* *Level 1 (TRAINED)*: Everything at standard
* *Level 2 (VETERAN)*: Time in-between salves = *85%*, Precision = *+15*, Suppress Damage = *75%*
* *Level 3 (ELITE*: Time in-between salves = *66%*, Precision = *+25*, Suppress Damage = *50%*

Furthermore, only armed units can gain Experience (described by *CanWinExperience*).\
As outlined in `Experience.ndf`, *ExperienceGainBySecond* and *ExperienceMultiplierBonusOnKill* are set to 0 and 1 equivalently. This means, at least for now, units are either not able to level up or they only gain experience by killing.

## Division Rules
Describes how every division is built up. For every unit in `DivisionRules.ndf` we have the following values.

`ref` **UnitDescriptor** &mdash; Reference to *UniteDescriptor.ndf*\
`bol` **AvailableWithoutTransport**\
`arr` **AvailableTransportList**\
`int` **MaxPackNumber** &mdash; How many cards you can take (varies per division)\
`int` **NumberOfUnitInPack** &mdash; How many units one card holds (Doesn't vary)\
`arr` **NumberOfUnitInPackXPMultiplier** &mdash; Multiply with *NumberOfUnitInPack* to get the amount of units per card at given veterancy level.

## Unit Descriptor
All useful values to be found in `UniteDescriptor.ndf`

### Every Unit Type
`str` **MotherCountry**\
`str` **AcknowUnitType**\
`flt` **UnitConcealmentBonus**\
`bol` **UnitIsStealth**\
`bol` **StunFreezesUnits**\
`ref` **MaxStunDamages**\
`ref` **StunDamagesRegen**\
`ref` **MaxSuppressionDamages**\
`ref` **SuppressDamagesRegenRatio**\
`str` **ArmorDescriptorFront** &mdash; Armor Front\
`str` **ArmorDescriptorSides** &mdash; Armor Side\
`str` **ArmorDescriptorRear** &mdash; Armor Rear\
`str` **ArmorDescriptorTop** &mdash; Armor Top\
`flt` **MaxDamages**\
`flt` **HitRollSize**\
`flt` **HitRollECM**\
`flt` **Dangerousness**\
`int` **MoralLevel**\
`int` **FuelCapacity**\
`flt` **FuelMoveDuration**\
`int` **PorteeVisionTBA**\
`int` **DetectionTBA**\
`int` **PorteeVision**\
`int` **OpticalStrength**\
`int` **OpticalStrengthAltitude**\
`bol` **UnitDetectStealthUnit**\
`flt` **IdentifyBaseProbability**\
`flt` **TimeBetweenEachIdentifyRoll**\
`int` **ProductionYear**\
`int` **ProductionTime**\
`int` **Resource_CommandPoints**\
`int` **Resource_Tickets**\
`str` **UpgradeFromUnit** &mdash; Predecessor

#### Ground Units Movement
`int` **MaxSpeed**\
`flt` **SpeedBonusOnRoad**\
`flt` **MaxAcceleration**\
`flt` **MaxDeceleration**\
`flt` **TempsDemiTour**\
`str` **VehicleSubType**

#### Air Units Movement
`int` **EvacuationTime**\
`int` **TravelDuration**

#### Supply Units
`flt` **SupplyCapacity**\
`int` **SupplyPriority**

#### Label
`bol` **IsSupply**\
`bol` **IsBuilding**\
`bol` **IsTransporter**\
`bol` **IsCommandementUnit**\
`bol` **IsPlane**\
`bol` **IsParachutist**\
`str` **UnitName**

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`

`arr` **Salves** &mdash; Poorly understood\
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
* **eMeM** over on Discord for the calculation of the road speed and help with experience & veterancy
* **unipus** over on Discord for pointing me in the right direction to understand AP damage for kinetic weapons

## Copyright Notice
Each and every bit of this data belongs to [Eugen Systems](https://eugensystems.com/). I soley dig through it to create a database for an WARNO API that will be accessible to the public for free.
