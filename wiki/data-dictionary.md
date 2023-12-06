## Division Rules

Describes how every division is built up. For every unit in `DivisionRules.ndf` we have the following values.

<details><summary><kbd>ref</kbd> UnitDescriptor</summary><p>Reference to <b>UniteDescriptor.ndf</b></p></details>
<details><summary><kbd>bol</kbd> AvailableWithoutTransport</summary><p> </p></details>
<details><summary><kbd>arr</kbd> AvailableTransportList</summary><p> Array containing all available transports.</p></details>
<details><summary><kbd>int</kbd> MaxPackNumber</summary><p> How many cards of this unit type can be taken (varies per division)</p></details>
<details><summary><kbd>int</kbd> NumberOfUnitInPack</summary><p> How many units each card holds (does not vary per division)</p></details>
<details><summary><kbd>arr</kbd> NumberOfUnitInPackXPMultiplier</summary><p>  Multiply with <b>NumberOfUnitInPack</b> to get the amount of units per card at given veterancy level.</p></details>

## Unit Descriptor

All useful values to be found in `UniteDescriptor.ndf`

### General Information

<details><summary><kbd>str</kbd> Nationalite (Alliance)</summary><p>Can either be <b>ENationalite/Allied</b> (NATO) or <b>ENationalite/Axis</b> (PACT)</p></details>
<details><summary><kbd>str</kbd> MotherCountry (Nation)</summary><p> Can either be <b>SOV</b>, <b>US</b>, <b>UK</b>, <b>DDR</b>, <b>RFA</b> (West-Germany) or <b>BEL</b></p></details>
<details><summary><kbd>arr</kbd> RoleList (Quality)</summary><p> Can either be <b>tank_A</b> (A | Excellent), <b>tank_B</b> (B | Good), <b>tank_C</b> (C | Mediocre) or <b>tank_D</b> (D | Poor)</p></details>
<details><summary><kbd>str</kbd> Factory (Category)</summary><p> Can either be <b>Logistic</b> (LOG), <b>Infantry</b> (INF), <b>Support</b> (ART), <b>Tanks</b> (TNK), <b>Recons</b> (REC), <b>AT</b> (AA), <b>Helis</b> (HEL), <b>Planes</b> (AIR)</p></details>
<details><summary><kbd>arr</kbd> SpecialtiesList (Role)</summary><p>Can either be <b>hq</b> (Command unit), <b>supply</b>, <b>infantry</b> (Infantry Squad), <b>infantry_half</b> (Infantry Group), <b>engineer</b> (Assault Squad), <b>assault_half</b> (Assault Group), <b>mortar</b>, <b>howitzer</b>, <b>mlrs</b>, <b>ifv</b> (Infantry Fightung Vehicle), <b>armor</b> (Main Battle Tank), <b>reco</b>, <b>hel_recp</b> (Helicopter Reconnaissance), <b>appui</b> (Support), <b>AT</b> (Anti-Tank), <b>transport</b>, <b>AA</b> (Air Defence) or <b>sead</b></p></details>
<details><summary><kbd>int</kbd> ProductionYear</summary><p></p></details>
<details><summary><kbd>int</kbd> ProductionTime</summary><p> <b>5</b> for every unit except <b>-1</b> for planes. I think it's the time between placing units and them spawning in.</p></details>
<details><summary><kbd>int</kbd> Resource_CommandPoints</summary><p></p></details>
<details><summary><kbd>str</kbd> UpgradeFromUnit</summary><p> Predecessor</p></details>
<details><summary><kbd>des</kbd> TInfluenceScoutModuleDescriptor (Reveal Influenece)</summary><p> Descriptor is empty for every unit, however, if its header is present it triggers <b>Reveal Influenece</b> to be set to <b>yes</b> in the in-game armory. Furthermore, it will show you the blue/red dividing lines when a zone is contested, helping you to guess the enemy command vehicle's (CVs) location.</p></details>
<details><summary><kbd>flt</kbd> DeploymentShift</summary><p> If the descriptor is present it states how far the unit can be forward deployed.</p></details>

### Damage

<details><summary><kbd>ref</kbd> StunDamagesRegen</summary><p> </p></details>
<details><summary><kbd>ref</kbd> MaxStunDamages</summary><p> </p></details>
<details><summary><kbd>ref</kbd> SuppressDamagesRegenRatio</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>ref</kbd> SuppressDamagesRegenRatioOutOfRange</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>ref</kbd> MaxSuppressionDamages</summary><p>Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>flt</kbd> MaxDamages (Strength)</summary><p>The unit's health. In-game called <b>strength</b> for infantry units. Note that increasing strength does not automatically increase the squad's size. You would need to adjust <b>NbSoldatInGroupeCombat</b> and <b>Depiction</b> aswell.</p></details>
<details><summary><kbd>ref</kbd> WeaponManager</summary><p>Reference to <b>WeaponDescriptor.ndf</b></p></details>

### Armor

<details><summary><kbd>str</kbd> ArmorDescriptorFront</summary><p> Armor Front</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorSides</summary><p> Armor Side</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorRear</summary><p> Armor Rear</p></details>
<details><summary><kbd>str</kbd> ArmorDescriptorTop</summary><p> Armor Top</p></details>

### Visibility & Targetability

<details><summary><kbd>int</kbd> OpticalStrength</summary><p> Optics for ground units. Presumably used to determine whether a unit can see enemy units in cover: can either be <b>40</b> (Bad), <b>60</b> (Mediocre), <b>80</b> (Normal), <b>120</b> (Good), <b>170</b> (Very Good) or <b>220</b> (Exceptional)</p></details>
<details><summary><kbd>int</kbd> OpticalStrengthAltitude</summary><p> Optics for air targets. This value is not represented on the in-game UI and does not count towards <b>OpticalStrength</b>.</p></details>
<details><summary><kbd>flt</kbd> IdentifyBaseProbability</summary><p> <b>Guess</b>: I think <b>OpticalStrength</b> defines how well units can be seen, <b>IdentifyBaseProbability</b> is the probability that these units can be uniquely identified.</p></details>
<details><summary><kbd>flt</kbd> TimeBetweenEachIdentifyRoll</summary><p><b>Guess</b>: Time in-between trying to uniquely identify units.</p></details>
<details><summary><kbd>flt</kbd> UnitConcealmentBonus (Stealth)</summary><p> In-game called <b>stealth</b>. Can either be <b>1.0</b> (Bad), <b>1.5</b> (Mediocre), <b>2.0</b> (Good) or <b>2.5</b> (Exceptional)</p></details>
<details><summary><kbd>flt</kbd> HitRollECM</summary><p> Multiplier for hit probability. 0 means no Electronic countermeasures (ECM)</p></details>
<details><summary><kbd>int</kbd> PorteeVision</summary><p> Maximum range at which a unit can see an unidentified ground unit. This variable is set to <b>10000</b> except for SEAD planes it is higher.</p></details>
<details><summary><kbd>flt</kbd> PorteeVisionTBA</summary><p> Set to <b>0</b> for every unit except <b>14000</b> for planes.</p></details>
<details><summary><kbd>flt</kbd> PorteeVisionFOW</summary><p> Set to <b>0</b> for every unit except <b>1600</b> for helicopters.</p></details>
<details><summary><kbd>flt</kbd> DetectionTBA</summary><p> Maximum range at which a unit can see an unidentified helicopter. Set to <b>14000</b> for every unit.</p></details>

### Strategic

<details><summary><kbd>int</kbd> UnitAttackValue</summary><p> Might be used for AI.</p></details>
<details><summary><kbd>int</kbd> UnitDefenseValue</summary><p> Might be used for AI.</p></details>
<details><summary><kbd>flt</kbd> Dangerousness</summary><p> Might be used by AI to determine which unit to engage first.</p></details>

### Orders

<details><summary><kbd>ref</kbd> UnlockableOrders</summary><p> Reference to <b>OrderAvailability_Tactic.ndf</b>. Contains a list of orders that can be given to this particular unit.</p></details>

### Label

<details><summary><kbd>bol</kbd> IsTransporter</summary><p> </p></details>
<details><summary><kbd>bol</kbd> IsPlane</summary><p> </p></details>

### Fuel

<details><summary><kbd>int</kbd> FuelCapacity</summary><p> How many liters of fuel a unit can hold.</p></details>
<details><summary><kbd>flt</kbd> FuelMoveDuration</summary><p>  How many seconds a unit can move before running out of fuel. Described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#calculate-autonomy"> Calculate Autonomy</a> </p></details>

### Special to Ground Units

<details><summary><kbd>int</kbd> MaxSpeed</summary><p> </p></details>
<details><summary><kbd>flt</kbd> SpeedBonusOnRoad</summary><p> </p></details>
<details><summary><kbd>flt</kbd> MaxAcceleration</summary><p> </p></details>
<details><summary><kbd>flt</kbd> MaxDeceleration</summary><p> </p></details>
<details><summary><kbd>flt</kbd> TempsDemiTour</summary><p> The amount of seconds it takes for a unit to make a half-turn.</p></details>
<details><summary><kbd>str</kbd> VehicleSubType</summary><p> </p></details>

### Special to Planes

<details><summary><kbd>int</kbd> EvacuationTime</summary><p> </p></details>
<details><summary><kbd>int</kbd> TravelDuration</summary><p> </p></details>
<details><summary><kbd>int</kbd> Altitude</summary><p> Preferred flying altitude</p></details>
<details><summary><kbd>ref</kbd> AltitudeMax</summary><p> Reference to <b>AirplaneConstantes.ndf</b>; always set to <b>10000 * Metre</b></p></details>
<details><summary><kbd>int</kbd> AltitudeMin</summary><p> Minimum flying altitude; will break off from certain attacks if they involve going deeper.</p></details>
<details><summary><kbd>ref</kbd> AltitudeMinForRoll</summary><p> Reference to <b>AirplaneConstantes.ndf</b>; always set to <b>2000 * Metre</b></p></details>
<details><summary><kbd>ref</kbd> MinRollSpeedForRoll</summary><p> Reference to <b>AirplaneConstantes.ndf</b>; always set to <b>65°/s</b></p></details>
<details><summary><kbd>int</kbd> AgilityRadius</summary><p> I believe it to be the equivalent of <b>TempsDemiTour</b> for planes; states the turn radius. Certainly determines the agility of the plane in question.</p></details>
<details><summary><kbd>int</kbd> PitchAngle</summary><p> </p></details>
<details><summary><kbd>ref</kbd> PitchSpeed</summary><p> </p></details>
<details><summary><kbd>int</kbd> RollAngle</summary><p> </p></details>
<details><summary><kbd>int</kbd> RollSpeed</summary><p> </p></details>

### Special to Helicopters

<details><summary><kbd>int</kbd> UpwardSpeed</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>int</kbd> TorqueManoeuvrability</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>int</kbd> CyclicManoeuvrability</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>int</kbd> MaxInclination</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>flt</kbd> GFactorLimit</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>int</kbd> RotorArea</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>
<details><summary><kbd>int</kbd> Mass</summary><p> Controls movement in some way, though in what way is uncertain.</p></details>

### Special to Infantry Units

<details><summary><kbd>int</kbd> NbSoldatInGroupeCombat</summary><p> The squad's size in number of soldiers.</p></details>

### Special to Supply Units

<details><summary><kbd>flt</kbd> SupplyCapacity</summary><p> How many supplies this unit is carrying.</p></details>

### Probably Not Important

<details><summary><kbd>flt</kbd> HitRollSize</summary><p> Size does no longer effect hit chance-to-hit.</p></details>
<details><summary><kbd>int</kbd> MoralLevel</summary><p> Reason not included is described in chapter<a href="https://github.com/BE3dARt/WARNO-DATA#stress-suppression-cohesion-and-morale"> Stress, Suppression, Cohesion and Morale</a></p></details>
<details><summary><kbd>bol</kbd> IsParachutist</summary><p> Currently set to <b>False</b> for every unit.</p></details>
<details><summary><kbd>int</kbd> Resource_Tickets</summary><p> Could be used as prices for future campaigns.</p></details>
<details><summary><kbd>int</kbd> CommanderLevel</summary><p> Only present on command units. However, it is set to <b>1</b> for every unit that has it.</p></details>
<details><summary><kbd>bol</kbd> UnitIsStealth</summary><p> <b>False</b> for every unit. Stealth is defined by <b>UnitConcealmentBonus</b>.</p></details>
<details><summary><kbd>tkn</kbd> UnitName</summary><p> Unfortunately we can't decode tokens yet.</p></details>
<details><summary><kbd>int</kbd> SupplyPriority</summary><p> Used in WGRD to state how many other supply units this unit could itself draw supplies from. Set to <b>-1</b> for every unit.</p></details>
<details><summary><kbd>int</kbd> UnitBonusXpPerLevelValue</summary><p> Set to <b>1</b> for every unit except aircraft.</p></details>

## Weapon Descriptor

All useful values to be found in `WeaponDescriptor.ndf`. A weapon system (_TWeaponManagerModuleDescriptor_) consist of multiple turret descriptors (_TTurretInfanterieDescriptor_ or _TTurretTwoAxisDescriptor_). These turrets have one or multiple weapons attached to it (_TMountedWeaponDescriptor_), each having its own ammunition defined in `Ammunition.ndf`.

<details><summary><kbd>arr</kbd> Salves</summary><p> Array holding multiple ammunition pools. An ammunition pool defines the total number of salvos a weapon (which pulls salvos from this pool) can fire before running out of ammunition.</p></details>
<details><summary><kbd>int</kbd> NbWeapons</summary><p> The unit's quantity of this specific weapons. Primarily used on infantry units.</p></details>
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

### Probably Not Important

<details><summary><kbd>flt</kbd> IsAPCR</summary><p> Probably used when Armour-piercing, composite rigid (APCR) (high-velocity armour-piercing (HVAP) in US nomenclature) are implemented into WARNO. Removed in game version 80721.</p></details>
