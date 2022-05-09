## Introduction
Eugen Systems have published their raw game data of WARNO for the first time in their Milestone MURAT. This project aims at understanding and interpreting these values for the ultimate goal: **WARNO API**

Through the whole documentary disclosure widgets, like the following, can be found. Click them to get information on the given variable.
<details><summary><kbd>type</kbd> Click me to open the widget!</summary><p>Have fun!</p></details>

## Useful Information
WARNO has some twists and turns when it comes down to comprehensibility. These are some useful tools to guide you through the jungle of WARNO data.

### Constant Factors
Some values presented in `.ndf` files need to be multiplied by a constant factor. I know of **two** constants so far that are defined in `GDConstantes.ndf`:
* MultiplicateurMetreRTSVersDistanceFeedbackTactique: **1.0 div 2.83** &mdash; Needs to be multiplied with the *distance* to receive accurate results. E.g. 6000 m \* (**1.0 / 2.83**) = 2120 m
* MultiplicateurMetreRTSVersVitesseTactiquePourVehicule: **0.45 div 1.0** &mdash; Needs to be multiplied with the *speed* to receive accurate results. E.g. 120 km/h \* (**0.45 / 1.0**) = 54 km/h

### Calculate Road Speed
In `UniteDescriptor.ndf` there are values called *VitesseCombat* and *RealRoadSpeed* which are not being used. Instead, we should use *MaxSpeed* which represents the off-road speed. Compute (*MaxSpeed* + *MaxSpeed* \* *SpeedBonusOnRoad*) \* *MultiplicateurMetreRTSVersVitesseTactiquePourVehicule* to get the true road speed.

### Calculate Autonomy
Autonomy states how far a unit can move until it runs out of fuel. In previous titles, this was measured in seconds, however, in WARNO it is specifically stated in *kilometres*. For planes, *Autonomy* is equivalent to their *FuelMoveDuration*. For ground units, the following calculation holds very well. Be aware that this calculation was created using multiple results and searching a common pattern, hence the strange factor. Round up to the nearest integer if the first decimal place of the result is bigger than 5.

*Autonomy* = *MaxSpeed* \* *FuelMoveDuration* \* *0.0000975*

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

### Stress, Suppression, Cohesion and Morale
**Stress** and **suppression** are one and the same variable. In-game it is called *stress* and in the `.ndf` files it is mostly called *suppression*. Unlike Wargame: Red Dragon, this value is not shown in the WARNO UI. Instead, the current cohesion level is displayed.\
**Moral** is poorly understood. The fact that it is only non-zero for planes makes it hard to believe that it is a system that has any impact in-game, if any. It might very well be a leftover from a previous game.\
**Cohesion** is a direct effect of suppression. There are four levels which are described in `EffetsSurUnite.ndf`. Each comes with its own debuffs.

Which suppression system is being used is individually defined in `UniteDescriptor.ndf` under *SuppressDamageLevelsPack*. This variable is a reference to `DamageLevels.ndf` in which the following can be found: Every system has six different suppression levels (*calm*, *engaged*, *worried*, *stressed*, *shaken* and (*panicked* or *pinned*)), being triggered at different suppress damage levels defined by *Value*. Note that *Value* is most likely only the modifier for another variable, like the maximum amount of suppression damage. Each suppression level comes with custom debuffs: Morale is being modified (*MoralModifier*), chance of hitting the target is decreased (*HitRollModifier*) and *EffectsPacks* are being added. *EffectsPacks* can hold multiple effects, but the most important is the cohesion being changed. Its debuffs are outlined in `EffetsSurUnite.ndf`.

Suppression damage decreases over time. The following variables describe this behavior. They can be found in `UniteDescriptor.ndf` for every unit and are all references to `DamageModules.ndf`.
* *GroundUnit_SuppressDamagesRegenRatioList*: Array detailing how much suppression damage is being recovered over a given time period: *[Time, Suppression damage recovered]*
* *GroundUnit_SuppressDamagesRegenRatioOutOfRange*: How many seconds need to pass until suppression damage recovery starts.
* *GroundUnit_MaxSuppressionDamages*: Maximum suppression damage that can be received, however, it is unknown what happens if this threshold is being exceeded.

*SuppressDamages* in `Ammunition.ndf` describes how much suppress damage a weapon can generate. I strongly believe that the amount of suppress damage *received* is the same for all units because *MaxSuppressionDamages* is set to 1000 for every unit type and there is no multiplier mentioned in `UniteDescriptor.ndf` whatsoever.

## Division Rules
Describes how every division is built up. For every unit in `DivisionRules.ndf` we have the following values.

`ref` **UnitDescriptor** &mdash; Reference to *UniteDescriptor.ndf*\
`bol` **AvailableWithoutTransport**\
`arr` **AvailableTransportList** &mdash; Array containing all available transports.\
`int` **MaxPackNumber** &mdash; How many cards you can take (varies per division)\
`int` **NumberOfUnitInPack** &mdash; How many units one card holds (Doesn't vary)\
`arr` **NumberOfUnitInPackXPMultiplier** &mdash; Multiply with *NumberOfUnitInPack* to get the amount of units per card at given veterancy level.

## Unit Descriptor
All useful values to be found in `UniteDescriptor.ndf`

### General Information
<details><summary><kbd>str</kbd> Nationalite</summary><p> Alliance: can either be <b>ENationalite/Allied</b> (NATO) or <b>ENationalite/Axis</b> (PACT)</p></details>
<details><summary><kbd>str</kbd> MotherCountry</summary><p> Nation: can either be <b>SOV</b>, <b>US**, <b>UK</b>, <b>DDR</b>, <b>RFA</b> (West-Germany) or <b>BEL</b></p></details>
<details><summary><kbd>arr</kbd> RoleList</summary><p> Quality: can either be <b>tank_A</b> (A | Excellent), <b>tank_B</b> (B | Good), <b>tank_C</b> (C | Mediocre) or <b>tank_D</b> (D | Poor)</p></details>
<details><summary><kbd>str</kbd> Factory</summary><p> Category: can either be <b>Logistic** (LOG), <b>Infantry</b> (INF), <b>Support</b> (ART), <b>Tanks</b> (TNK), <b>Recons</b> (REC), <b>AT</b> (AA), <b>Helis</b> (HEL), <b>Planes</b> (AIR)</p></details>
<details><summary><kbd>arr</kbd> SpecialtiesList</summary><p> Role: can either be <b>hq</b> (Command unit), <b>supply</b>, <b>infantry</b> (Infantry Squad), <b>infantry_half</b> (Infantry Group), <b>engineer</b> (Assault Squad), <b>assault_half</b> (Assault Group), <b>mortar</b>, <b>howitzer</b>, <b>mlrs</b>, <b>ifv</b> (Infantry Fightung Vehicle), <b>armor</b> (Main Battle Tank), <b>reco</b>, <b>hel_recp</b> (Helicopter Reconnaissance), <b>appui</b> (Support), <b>AT</b> (Anti-Tank), <b>transport</b>, <b>AA</b> (Air Defence) or <b>sead</b></p></details>
<details><summary><kbd>int</kbd> ProductionYear</summary><p></p></details>
<details><summary><kbd>int</kbd> Resource_CommandPoints</summary><p></p></details>
<details><summary><kbd>str</kbd> UpgradeFromUnit</summary><p> Predecessor</p></details>

### Damage
<details><summary><kbd>ref</kbd> StunDamagesRegen</summary><p> </p></details>
<details><summary><kbd>ref</kbd> MaxStunDamages</summary><p> </p></details>
<details><summary><kbd>ref</kbd> SuppressDamagesRegenRatio</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>ref</kbd> SuppressDamagesRegenRatioOutOfRange</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>ref</kbd> MaxSuppressionDamages</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>flt</kbd> MaxDamages</summary><p>In-game called <b>strength</b> for infantry units</p></details>

### Armor
<details><summary><kbd>str</kbd> ArmorDescriptorFront</summary><p>Armor Front</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorSides</summary><p>Armor Side</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorRear</summary><p>Armor Rear</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorTop</summary><p>Armor Top</p></details>

### Visibility & Targetability
`int` **OpticalStrength** &mdash; Optics for ground units. Presumably used to determine whether a unit can see enemy units in cover: can either be **40** (Bad), **60** (Mediocre), **80** (Normal), **120** (Good), **170** (Very Good) or **220** (Exceptional)\
`int` **OpticalStrengthAltitude** &mdash; Optics for air targets. This value is not represented on the in-game UI and does not count towards *OpticalStrength*.\
`flt` **IdentifyBaseProbability** &mdash; *Guess*: I think *OpticalStrength* defines how well units can be seen, *IdentifyBaseProbability* is the probability that these units can be uniquely identified.\
`flt` **TimeBetweenEachIdentifyRoll**&mdash; *Guess*: Time in-between trying to uniquely identify units.\
`flt` **UnitConcealmentBonus**&mdash; In-game called *stealth*. Can either be **1.0** (Bad), **1.5** (Mediocre), **2.0** (Good) or **2.5** (Exceptional)\
`flt` **HitRollECM** &mdash; Multiplier for hit probability. 0 means no Electronic countermeasures (ECM)

### Strategic
`int` **UnitAttackValue** &mdash; Might be used for AI.\
`int` **UnitDefenseValue** &mdash; Might be used for AI.\
`flt` **Dangerousness** &mdash; Might be used by AI to determine which unit to engage first.

### Fuel
`int` **FuelCapacity** &mdash; How many liters of fuel a unit can hold\
`flt` **FuelMoveDuration** &mdash; How many seconds a unit can move before running out of fuel. Described in chapter [Calculate Autonomy](https://github.com/BE3dARt/WARNO-DATA#calculate-autonomy)

#### Special to Ground Units
`int` **MaxSpeed**\
`flt` **SpeedBonusOnRoad**\
`flt` **MaxAcceleration**\
`flt` **MaxDeceleration**\
`flt` **TempsDemiTour** &mdash; The amount of seconds it takes for a unit to make a half-turn.\
`str` **VehicleSubType**

#### Special to Planes
`int` **EvacuationTime**\
`int` **TravelDuration**

#### Supply Units
`flt` **SupplyCapacity**\
`int` **SupplyPriority**

#### Label
`bol` **IsTransporter**\
`str` **UnitName**

#### Not Used
`flt` **HitRollSize** &mdash; Size does no longer effect hit propability.\
`int` **MoralLevel** Reason not included is described in chapter [Stress, Suppression, Cohesion and Morale](https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale)\
`int` **ProductionTime** *5* for every unit except *-1* for planes. I think it's the time between placing units and them spawning in.\
`des` **TInfluenceScoutModuleDescriptor** Empty for every unit but if present it triggers *Reveal Influenece* to be *yes* in-game.\
`bol` **IsParachutist** &mdash; Currently set to *False* for every unit.\
`int` **Resource_Tickets** &mdash; Could be used as prices for future campaigns.

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`. A weapon system (*TWeaponManagerModuleDescriptor*) consist of multiple turret descriptors (*TTurretInfanterieDescriptor* or *TTurretTwoAxisDescriptor*). These turrets have one or multiple weapons attached to it (*TMountedWeaponDescriptor*), each having its own ammunition defined in `Ammunition.ndf`.

`arr` **Salves** &mdash; Array holding multiple ammunition pools. An ammunition pool defines the total number of salvos a weapon can fire before running out of ammunition.\
`int` **SalvoStockIndex** &mdash; Defines which ammunition pool (*Savles*) is being used by this specific weapon. E.g. tank cannons have separate weapon descriptors for HE and AP but will pull from the same ammunition pool. Mod will not compile if *SalvoStockIndex* links to ammunition pools holding *0* or *-1*\
`ref` **Ammunition** &mdash; References an object in `Ammunition.ndf`\
`int` **YulBoneOrdinal** &mdash; Some kind of animation rig. It is safe to just increment it per turret descriptor.\
`int` **NbFx** &mdash; Number of graphics effects\
`bol` **HasMainSalvo** &mdash; Most likely useless\
`flt` **OutOfRangeTrackingDuration** &mdash; Function not known

## Ammunition Descriptor
All useful values to be found in `Ammunition.ndf`

`tkn` **Name**\
`tkn` **TypeCategoryName** &mdash; Weapon description like *Heavy Machine Gun*, *Howitzer*, *etc.*. However, we can't resolve name tokens for now.\
`tkn` **Caliber**\
`str` **ProjectileType**\
`flt` **Puissance** &mdash; Function not known\
`flt` **TempsEntreDeuxTirs** &mdash; Time between two shots\
`int` **PorteeMinimale** &mdash; Maximal engagement distance (Ground)\
`int` **PorteeMaximale** &mdash; Minimal engagement distance (Ground)\
`int` **PorteeMinimaleTBA** &mdash; Maximal engagement distance (Helicopter)\
`int` **PorteeMaximaleTBA** &mdash; Minimal engagement distance (Helicopter)\
`int` **PorteeMinimaleHA** &mdash; Maximal engagement distance (Planes)\
`int` **PorteeMaximaleHA** &mdash; Minimal engagement distance (Planes)\
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
`bol` **PiercingWeapon** &mdash; Function not known

## Special Thanks
I wanted to thank the following people. Whithout them, this project would have gone nowhere:
* **eMeM** over on Discord for the calculation of the road speed, a guess on recource tickets, help with experience & veterancy and the discussion over stress, suppression, cohesion and morale.
* **unipus** over on Discord for pointing me in the right direction to understand AP damage for kinetic weapons.
* **gagarin** over on Discord for helping me finding the filter by category.
* **Terminus Est** over on Discord for defining *Salves*, *SalvoStockIndex*, *YulBoneOrdinal*, *NbFx*, *HasMainSalvo* and *OutOfRangeTrackingDuration* in `WeaponDescriptor.ndf`.

## Copyright Notice
Each and every bit of this data belongs to [Eugen Systems](https://eugensystems.com/). I soley dig through it to create a database for an WARNO API that will be accessible to the public for free.
