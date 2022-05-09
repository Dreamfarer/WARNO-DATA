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
<details><summary><kbd>str</kbd> Nationalite (Alliance)</summary><p>Can either be <b>ENationalite/Allied</b> (NATO) or <b>ENationalite/Axis</b> (PACT)</p></details>
<details><summary><kbd>str</kbd> MotherCountry (Nation)</summary><p> Can either be <b>SOV</b>, <b>US</b>, <b>UK</b>, <b>DDR</b>, <b>RFA</b> (West-Germany) or <b>BEL</b></p></details>
<details><summary><kbd>arr</kbd> RoleList (Quality)</summary><p> Can either be <b>tank_A</b> (A | Excellent), <b>tank_B</b> (B | Good), <b>tank_C</b> (C | Mediocre) or <b>tank_D</b> (D | Poor)</p></details>
<details><summary><kbd>str</kbd> Factory (Category)</summary><p> Can either be <b>Logistic</b> (LOG), <b>Infantry</b> (INF), <b>Support</b> (ART), <b>Tanks</b> (TNK), <b>Recons</b> (REC), <b>AT</b> (AA), <b>Helis</b> (HEL), <b>Planes</b> (AIR)</p></details>
<details><summary><kbd>arr</kbd> SpecialtiesList (Role)</summary><p>Can either be <b>hq</b> (Command unit), <b>supply</b>, <b>infantry</b> (Infantry Squad), <b>infantry_half</b> (Infantry Group), <b>engineer</b> (Assault Squad), <b>assault_half</b> (Assault Group), <b>mortar</b>, <b>howitzer</b>, <b>mlrs</b>, <b>ifv</b> (Infantry Fightung Vehicle), <b>armor</b> (Main Battle Tank), <b>reco</b>, <b>hel_recp</b> (Helicopter Reconnaissance), <b>appui</b> (Support), <b>AT</b> (Anti-Tank), <b>transport</b>, <b>AA</b> (Air Defence) or <b>sead</b></p></details>
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
<details><summary><kbd>str</kbd> ArmorDescriptorFront</summary><p> Armor Front</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorSides</summary><p> Armor Side</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorRear</summary><p> Armor Rear</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorTop</summary><p> Armor Top</p></details>

### Visibility & Targetability
<details><summary><kbd>int</kbd> OpticalStrength</summary><p> Optics for ground units. Presumably used to determine whether a unit can see enemy units in cover: can either be <b>40</b> (Bad), <b>60</b> (Mediocre), <b>80</b> (Normal), <b>120</b> (Good), <b>170</b> (Very Good) or <b>220</b> (Exceptional)</p></details>
<details><summary><kbd>int</kbd> OpticalStrengthAltitude</summary><p> Optics for air targets. This value is not represented on the in-game UI and does not count towards <b>OpticalStrength</b>.</p></details>
<details><summary><kbd>int</kbd> PorteeVision</summary><p> Maximum range at which a unit can see an unidentified ground unit. This variable is set to <b>10000</b> except for SEAD planes it is higher.</p></details>
<details><summary><kbd>flt</kbd> IdentifyBaseProbability</summary><p> <b>Guess</b>: I think <b>OpticalStrength</b> defines how well units can be seen, <b>IdentifyBaseProbability</b> is the probability that these units can be uniquely identified.</p></details>
<details><summary><kbd>flt</kbd> TimeBetweenEachIdentifyRoll</summary><p><b>Guess</b>: Time in-between trying to uniquely identify units.</p></details>
<details><summary><kbd>flt</kbd> UnitConcealmentBonus (Stealth)</summary><p> In-game called <b>stealth</b>. Can either be <b>1.0</b> (Bad), <b>1.5</b> (Mediocre), <b>2.0</b> (Good) or <b>2.5</b> (Exceptional)</p></details>
<details><summary><kbd>flt</kbd> HitRollECM</summary><p> Multiplier for hit probability. 0 means no Electronic countermeasures (ECM)</p></details>

### Strategic
`int` **UnitAttackValue** &mdash; Might be used for AI.\
`int` **UnitDefenseValue** &mdash; Might be used for AI.\
`flt` **Dangerousness** &mdash; Might be used by AI to determine which unit to engage first.

#### Label
`bol` **IsTransporter**\

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
<details><summary><kbd>flt</kbd> SupplyCapacity</summary><p> How many supplies this unit is carrying.</p></details>

#### Probably Not Important
<details><summary><kbd>flt</kbd> HitRollSize</summary><p> Size does no longer effect hit chance-to-hit.</p></details>
<details><summary><kbd>int</kbd> MoralLevel</summary><p> Reason not included is described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>int</kbd> ProductionTime</summary><p> <b>5</b> for every unit except <b>-1</b> for planes. I think it's the time between placing units and them spawning in.</p></details>
<details><summary><kbd>des</kbd> TInfluenceScoutModuleDescriptor (Reveal Influenece)</summary><p> Empty for every unit but if present it triggers <b>Reveal Influenece</b> to be <b>yes</b> in-game.</p></details>
<details><summary><kbd>bol</kbd> IsParachutist</summary><p> Currently set to <b>False</b> for every unit.</p></details>
<details><summary><kbd>int</kbd> Resource_Tickets</summary><p> Could be used as prices for future campaigns.</p></details>
<details><summary><kbd>int</kbd> CommanderLevel</summary><p> Only present on command units. However, it is set to <b>1</b> for every unit that has it.</p></details>
<details><summary><kbd>bol</kbd> UnitIsStealth</summary><p> <b>False</b> for every unit. Stealth is defined by <b>UnitConcealmentBonus</b>.</p></details>
<details><summary><kbd>tkn</kbd> UnitName</summary><p> Unfortunately we can't decode tokens yet.</p></details>
<details><summary><kbd>flt</kbd> PorteeVisionTBA</summary><p> Set to <b>0</b> for every unit except <b>14000</b> for planes.</p></details>
<details><summary><kbd>flt</kbd> PorteeVisionFOW</summary><p> Set to <b>0</b> for every unit except <b>1600</b> for helicopters.</p></details>
<details><summary><kbd>flt</kbd> DetectionTBA</summary><p> Maximum range at which a unit can see an unidentified helicopter. Set to <b>14000</b> for every unit.</p></details>
<details><summary><kbd>int</kbd> SupplyPriority</summary><p> Used in WGRD to state how many other supply units this unit could itself draw supplies from. Set to <b>-1</b> for every unit.</p></details>

## Weapon Descriptor
All useful values to be found in `WeaponDescriptor.ndf`. A weapon system (*TWeaponManagerModuleDescriptor*) consist of multiple turret descriptors (*TTurretInfanterieDescriptor* or *TTurretTwoAxisDescriptor*). These turrets have one or multiple weapons attached to it (*TMountedWeaponDescriptor*), each having its own ammunition defined in `Ammunition.ndf`.

<details><summary><kbd>arr</kbd> Salves</summary><p> Array holding multiple ammunition pools. An ammunition pool defines the total number of salvos a weapon (which pulls salvos from this pool) can fire before running out of ammunition.</p></details>
<details><summary><kbd>int</kbd> SalvoStockIndex</summary><p> Defines which ammunition pool (<b>Savles</b>) is being used by this specific weapon. E.g. tank cannons have separate weapon descriptors for HE and AP but will pull from the <b>same</b> ammunition pool.</p></details>
<details><summary><kbd>bol</kbd> HasMainSalvo</summary><p> Only set to <b>True</b> for planes. It signifies that this plane has a ammunition pool (<b>Salves</b>) that, if empty, makes the plane evac winchester.</p></details>
<details><summary><kbd>arr</kbd> SalvoIsMainSalvo</summary><p> Only has a <b>True</b> in it for planes. States which ammunition pool (<b>Salves</b>) makes the plane evac winchester when empty.</p></details>
<details><summary><kbd>ref</kbd> Ammunition</summary><p> References an object in <b>Ammunition.ndf</b>.</p></details>
<details><summary><kbd>flt</kbd> AngleRotationMax</summary><p> Maximal traverse of turret in radians. Calculation as follows: <b>angle_degrees</b> = <b>angle_radians</b> \* <b>180°</b> / <b>pi</b></p></details>
<details><summary><kbd>flt</kbd> AngleRotationMaxPitch</summary><p> Maximum turret elevation in radians. Calculation as follows: <b>angle_degrees</b> = <b>angle_radians</b> \* <b>180°</b> / <b>pi</b></p></details>
<details><summary><kbd>flt</kbd> AngleRotationMinPitch</summary><p> Minimum turret depression in radians. Calculation as follows: <b>angle_degrees</b> = <b>angle_radians</b> \* <b>180°</b> / <b>pi</b></p></details>
<details><summary><kbd>flt</kbd> VitesseRotation</summary><p> Traverse speed of the turret, presumably in radians per second.</p></details>

## Ammunition Descriptor
All useful values to be found in `Ammunition.ndf`.

<details><summary><kbd>tkn</kbd> Name</summary><p> Ammunition name; unfortunately we can't decode tokens yet.</p></details>
<details><summary><kbd>tkn</kbd> TypeCategoryName</summary><p> Weapon description like <b>Heavy Machine Gun</b>, <b>Howitzer</b>, <b>etc</b>. Unfortunately we can't decode tokens yet.</p></details>
<details><summary><kbd>tkn</kbd> Caliber</summary><p> Caliber; unfortunately we can't decode tokens yet.</p></details>
<details><summary><kbd>arr</kbd> TraitsToken</summary><p> Will be added soon!</p></details>
<details><summary><kbd>int</kbd> Level</summary><p> Controls to which card slot this ammunition is assigned to</p></details>
<details><summary><kbd>ref</kbd> Arme</summary><p> How much armor-piercing (AP) damage is dealt. Read through chapter<a href="https://github.com/BE3dARt/WARNO-DATA#armor-piercing-ap-damage"> Armor-Piercing (AP) Damage</a> to get a detailed damage description and how to read this value correctly.</p></details>
<details><summary><kbd>flt</kbd> Puissance</summary><p> How noisy the weapon is. This variable is a stealth-negating multiplier that controls how much easier this unit is to spot when it fires this weapon.</p></details>
<details><summary><kbd>int</kbd> ShotsBeforeMaxNoise</summary><p> Either shot count until <b>Puissance</b> is in its full effect or there is a global maximum noise</p></details>
<details><summary><kbd>int</kbd> NbTirParSalves</summary><p> Shot count per magazine (salvo)</p></details>
<details><summary><kbd>flt</kbd> TempsEntreDeuxTirs</summary><p> Time in-between two shots until magazine (one salvo) is empty. For weapons that have a salvo size of one, e.g. tank cannons, this variable will be ignored. Presumably, this variable is <b>NOT</b> effected by decreasing morale (If it even exists in WARNO).</p></details>
<details><summary><kbd>flt</kbd> TempsEntreDeuxSalves</summary><p> Time in-between two salvos, a.k.a reload time. Presumably, this variable is effected by decreasing morale (If it even exists in WARNO).</p></details>
<details><summary><kbd>int</kbd> PorteeMaximale</summary><p> Maximal range against ground units.</p></details>
<details><summary><kbd>int</kbd> PorteeMinimale</summary><p> Minimum range against ground units.</p></details>
<details><summary><kbd>int</kbd> PorteeMaximaleTBA</summary><p> Maximal range against helicopters.</p></details>
<details><summary><kbd>int</kbd> PorteeMinimaleTBA</summary><p> Minimum range against helicopters.</p></details>
<details><summary><kbd>int</kbd> PorteeMaximaleHA</summary><p> Maximal range against planes.</p></details>
<details><summary><kbd>int</kbd> PorteeMinimaleHA</summary><p> Minimum range against planes.</p></details>
<details><summary><kbd>flt</kbd> AltitudeAPorteeMaximale</summary><p> Function unknown; exists for every ammunition type except missiles</p></details>
<details><summary><kbd>flt</kbd> AltitudeAPorteeMinimale</summary><p> Function unknown; exists for every ammunition type except missiles</p></details>
<details><summary><kbd>bol</kbd> AffecteParNombre</summary><p> Function unknown; exists for every ammunition type except missiles</p></details>
<details><summary><kbd>flt</kbd> AngleDispersion</summary><p> How much the ammunition spreads on impact or near-miss.</p></details>
<details><summary><kbd>int</kbd> DispersionAtMaxRange</summary><p> Dispersion at maximum range</p></details>
<details><summary><kbd>int</kbd> DispersionAtMinRange</summary><p> Dispersion at minimum range</p></details>
<details><summary><kbd>int</kbd> RadiusSplashPhysicalDamages</summary><p> Area of effect (AeE) of HE damage</p></details>
<details><summary><kbd>flt</kbd> PhysicalDamages</summary><p> HE damage in case of direct hit</p></details>
<details><summary><kbd>int</kbd> RadiusSplashSuppressDamages</summary><p> Area of effect (AeE) of suppress damage</p></details>
<details><summary><kbd>flt</kbd> SuppressDamages</summary><p> Suppress damage in case of direct hit</p></details>
<details><summary><kbd>int</kbd> RayonPinned</summary><p> Function unknown</p></details>
<details><summary><kbd>bol</kbd> AllowSuppressDamageWhenNoImpact</summary><p> Allow suppress damage to be dealt in case of near-miss.</p></details>
<details><summary><kbd>bol</kbd> TirIndirect</summary><p> <b>False</b> if this weapon is direct-fire.</p></details>
<details><summary><kbd>bol</kbd> TirReflexe</summary><p> Seems to be <b>False</b> for mortars, howitzers and bombs. Good chance that this is set to <b>True</b> if a weapon is able to target projectiles, hence <b>Reflexe</b>.</p></details>
<details><summary><kbd>bol</kbd> InterdireTirReflexe</summary><p> Prohibit <b>TirReflexe</b>. Good chance that is is the counter to whatever <b>TirReflexe</b> is.</p></details>
<details><summary><kbd>flt</kbd> NoiseDissimulationMalus</summary><p> Function unknown</p></details>
<details><summary><kbd>int</kbd> BaseCriticModifier</summary><p> Either set to <b>0</b> or <b>25</b>. Modifies the probability of triggering critial effects.</p></details>
<details><summary><kbd>int</kbd> EBaseHitValueModifier/Idling (Accuracy)</summary><p> Accuracy per shot while standing still. Accuracy in-game is displayed per salvo: <b>real_accuracy</b> = <b>EBaseHitValueModifier/Idling</b> \* <b>NbTirParSalves</b></p></details>
<details><summary><kbd>int</kbd> EBaseHitValueModifier/Moving (Accuracy)</summary><p> Accuracy per shot while moving. Accuracy in-game is displayed per salvo: <b>real_accuracy</b> = <b>EBaseHitValueModifier/Idling</b> \* <b>NbTirParSalves</b></p></details></p></details>
<details><summary><kbd>int</kbd> MaxSuccessiveHitCount</summary><p> Function unknown; Either set to <b>1</b> or <b>5</b></p></details>
<details><summary><kbd>flt</kbd> TempsDeVisee</summary><p> Aim time; How long, effected by morale (if existent), the unit needs time from seeing the enemy to being ready to engage it.</p></details>
<details><summary><kbd>flt</kbd> SupplyCost</summary><p> </p></details>
<details><summary><kbd>bol</kbd> CanShootOnPosition</summary><p> Used to define if button <b>Fire Pos</b> is available and therefore a unit is able to blindly fire without target at your request.</p></details>
<details><summary><kbd>bol</kbd> CanShootWhileMoving</summary><p> </p></details>
<details><summary><kbd>int</kbd> NbrProjectilesSimultanes</summary><p> Number of projectiles fired simultaneously</p></details>
<details><summary><kbd>ref</kbd> MissileDescriptor</summary><p> For missiles, this variable is a reference to <b>MissileDescriptors.ndf</b>, else it is set to <b>nil</b></p></details>
<details><summary><kbd>ref</kbd> SmokeDescriptor</summary><p> For smoke rounds, this variable is a reference to <b>SmokeDescriptor.ndf</b>, else it is set to <b>nil</b></p></details>
<details><summary><kbd>ref</kbd> FireDescriptor</summary><p> For incendiary rounds, this variable is a reference to <b>FireDescriptor.ndf</b>, else it is set to <b>nil</b></p></details>
<details><summary><kbd>bol</kbd> CanHarmInfantry</summary><p> </p></details>
<details><summary><kbd>bol</kbd> CanHarmVehicles</summary><p> </p></details>
<details><summary><kbd>bol</kbd> CanHarmHelicopters</summary><p> </p></details>
<details><summary><kbd>bol</kbd> CanHarmAirplanes</summary><p> </p></details>
<details><summary><kbd>bol</kbd> CanHarmGuidedMissiles</summary><p> </p></details>
<details><summary><kbd>bol</kbd> IsHarmlessForAllies</summary><p> </p></details>
<details><summary><kbd>bol</kbd> PiercingWeapon</summary><p> If ammunition is able to deal armor-piercing (AP) damage. Read through chapter<a href="https://github.com/BE3dARt/WARNO-DATA#armor-piercing-ap-damage"> Armor-Piercing (AP) Damage</a> to get a detailed damage description.</p></details>
<details><summary><kbd>ref</kbd> DamageTypeEvolutionOverRangeDescriptor</summary><p> If not <b>nil</b>, this variable references <b>DamageStairTypeEvolutionOverRangeDescriptor.ndf</b>, which handles armor-piercing (AP) damage decrease over distance. Moreover, this means that this ammunition is <b>kinetic</b>. Read through chapter<a href="https://github.com/BE3dARt/WARNO-DATA#armor-piercing-ap-damage"> Armor-Piercing (AP) Damage</a> to get a detailed damage description.</p></details>
<details><summary><kbd>flt</kbd> FlightTimeForSpeed</summary><p> Most likely used to calculate projectile speed together with <b>DistanceForSpeed</b></p></details>
<details><summary><kbd>flt</kbd> DistanceForSpeed</summary><p> Most likely used to calculate projectile speed together with <b>FlightTimeForSpeed</b></p></details>

#### Probably Not Important
<details><summary><kbd>flt</kbd> IsAPCR</summary><p> Probably used when Armour-piercing, composite rigid (APCR) (high-velocity armour-piercing (HVAP) in US nomenclature) are implemented into WARNO.</p></details>

## Special Thanks
I wanted to thank the following people. Whithout them, this project would have gone nowhere:
* **eMeM** over on Discord for the *calculation of the road speed*, a guess on *recource tickets*, definition of *CanShootOnPosition*, help with *experience & veterancy* and the discussion over *stress, suppression, cohesion and morale*.
* **unipus** over on Discord for pointing me in the right direction to understand *AP damage for kinetic weapons*.
* **gagarin** over on Discord for helping me finding the *filter by category*.
* **Iris** over on Discord for helping me getting *accuracy* right.
* **Terminus Est** over on Discord for defining *Salves*, *SalvoStockIndex*, *YulBoneOrdinal*, *NbFx*, *HasMainSalvo* and *OutOfRangeTrackingDuration* in `WeaponDescriptor.ndf`.

## Copyright Notice
Each and every bit of this data belongs to [Eugen Systems](https://eugensystems.com/). I soley dig through it to create a database for an WARNO API that will be accessible to the public for free.
