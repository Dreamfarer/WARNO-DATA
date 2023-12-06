## Constant Factors

Some values presented in `.ndf` files need to be multiplied by a constant factor. I know of **two** constants so far that are defined in `GDConstantes.ndf`:

- MultiplicateurMetreRTSVersDistanceFeedbackTactique: **1.0 div 2.83** &mdash; Needs to be multiplied with the _distance_ to receive accurate results. E.g. 6000 m \* (**1.0 / 2.83**) = 2120 m
- MultiplicateurMetreRTSVersVitesseTactiquePourVehicule: **0.45 div 1.0** &mdash; Needs to be multiplied with the _speed_ to receive accurate results. E.g. 120 km/h \* (**0.45 / 1.0**) = 54 km/h

## Damage Calculation

The unit's health pool is defined by **MaxDamages** in `UniteDescriptor.ndf`. It does not matter if _HE_ or _Penetration_ damage is dealt, ultimately ever damage type is converted into damage and subtracted from one and the same health pool (_MaxDamages_).

### Ammunition

We will be looking at **_Arme_** in `Ammunition.ndf`. This variables has two parts: _Family_ and _Index_. The _Family_ defines which damage type is being dealt. _Index_ on the other hand describes the weapon's 'power'. Please notice that _Index_ does not exactly mean the damage output, hence I used 'power', it is more of a variable used in the damage calculation. Usually you can read **_Arme_** out directly, but if your ammunition type is _kinetic_ AP, you absolutely need to adjust the _Index_ first because kinetic shells lose power over distance. Consult [this](#damage-reduction-for-kinetic-armor-piercing-ap) chapter to find out whether you are using _kinetic_ AP and how you would go about adjusting the _Index_.

Ultimately, **_Arme_** in `Ammunition.ndf` defines which damage scheme is being used by referencing another file called `DamageResistance.ndf`. In there a giant, overwhelming, but _very_ important table can be found: It lists every damage outcome of every weapon versus every armor:

- _Column_: Holds all damage types (Referenced by the before seen variable **_Arme_**)
- _row_: Holds the armor type

### Armor

As you see we need to figure out against which type of armor we are going up against before we are able to read out the table. For every unit armor is individually defined in `UniteDescriptor.ndf` by the variables **ArmorDescriptorFront**, **ArmorDescriptorSides**, **ArmorDescriptorRear** and **ArmorDescriptorTop**. These strings are referencing `ArmorDescriptor.ndf`, which translates them to the _row_ names of the giant table in `DamageResistance.ndf`.

The following armor types are actively being used by WARNO.

- **ArmorDescriptor_Batiment_1**: Used for buildings
- **ArmorDescriptor_Infanterie_1**: Used for Infantry; Can't receive armor-piercing (AP) damage, therefore in-game armory shows zero armor. However, there are multiple damage reductions present against various non-AP ammunition types.
- **ArmorDescriptor_Vehicule_1**: Used for vehicles; equivalent to _ArmorDescriptor_Blindage_1_.
- **ArmorDescriptor_Vehicule_leger**: Used for vehicles; Receives damage from **every** ammunition. Usually more than double the amount of damage received than _ArmorDescriptor_Vehicule_1_.
- **ArmorDescriptor_Blindage_1** to **ArmorDescriptor_Blindage_20**: Used for vehicles; Having blindage over 2 is utterly important: Going from _ArmorDescriptor_Blindage_1_ to _ArmorDescriptor_Blindage_2_ mostly **halves** the AP damage received. After that, it is only decreasing by small amounts.
- **ArmorDescriptor_Helico_1** to **ArmorDescriptor_Helico_3**: Used on helicopters and planes; _ArmorDescriptor_Helico_1_ is equivalent to _ArmorDescriptor_Blindage_1_. Using _ArmorDescriptor_Helico_2_ at least **halves** the damage received. After that, it is also only decreasing by small amounts.

### Calculation

We have the **row**, defined by **_Arme_** in `DamageResistance.ndf`, and the newly acquired **column**, defined in `UniteDescriptor.ndf` and translated in `ArmorDescriptor.ndf`. This enables us to pin-point one cell of this giant table.\
To conclude the damage calculation, retrieve the cell's value and multiply it with **PhysicalDamages** in `Ammunition.ndf` to get the actual damage dealt which will be subtract from the opponent's health pool.

### Damage Reduction for Kinetic Armor-Piercing (AP)

We need to consult `Ammunition.ndf` to check whether we are dealing with _kinetic_ AP. For this to be true, the _Family_ in the variable **_Arme_** needs to be set to _ap_ and **PiercingWeapon** must be set to _True_. If we are, we need to take its damage loss over range into consideration. In the in-game armory, the AP damage value is given at the weapon's maximum range. However, in `Ammunition.ndf` the AP damage value is given at point-blank range.

_AP_damage = AP_damage_point_blank - (range / factor)_

- _AP_damage_: Resulting AP damage
- _AP_damage_point_blank_: AP damage at point-blank equivalent to the index defined in varibale **_Arme_**
- _range_: Range to the enemy
- _factor_: Defined as the amount of AP damage decrease over a given range. To find this value we need to look at to what **DamageTypeEvolutionOverRangeDescriptor** is pointing to in `DamageStairTypeEvolutionOverRangeDescriptor.ndf`. For now, however, it is set to 1 AP damage reduction every 175m or 700m.

If you want to reproduce the values shown in the in-game armory, you would exchange _range_ with the weapon's maximum range defined by **PorteeMaximale**. Be aware, that this value is given in _metre_, so it has to be multiplied with the corresponding constant factor.

## Accuracy

Accuracy is defined as the probability of landing a successful shot on an enemy unit. Be aware that this whole accuracy system is not yet understood fully and assumptions are being made.\
To start off with a fact, _HitRollRuleDescriptor_ in `Ammunition.ndf` describes the accuracy for each ammunition type individually. This descriptor consists of:

- _BaseCriticModifier_
- _BaseEffectModifier_
- _BaseHitValueModifiers_
- _HitModifierList_

My best guess is that _BaseCriticModifier_ and _BaseEffectModifier_ are only used for the probability of triggering critical effects like "reseting targeting computer" and so on. We will ignore them both for now. What we are really interested in is _BaseHitValueModifiers_ and _HitModifierList_.

Now, for every shot a dice is rolled which will define if this particular shot is a hit or a miss. Just a random number would be too boring, we want to spice up the outcome with some parameters. My understanding is that _HitModifierList_ is exactly that: Parameters for the dice roll. This list consists of the following items: Precision, DistanceToTarget, SuccesiveShots and Suppress. Now, what do these mean? Do note though, these are pure guesses.

- _Precision_: It think it is the value when active _BaseHitValueModifiers_ are summed up. Basically this is the base chance of a hit. If the target has Electronic countermeasures (ECM), subtract its value from the base hit chance.
- _DistanceToTarget_: In `HitRollConstants.ndf` there is a list called _RangeModifiersTable_. It might state how to translate the distance to this parameter’s value. First off, you would calculate _distance_to_target_ / _weapon_maxRange_ to get a ratio which needs to be plugged into the left side of the list. Read out the corresponding right side to get the value for this parameter. So if the target is close to the attacker, it will yield a higher parameter value.
- _SuccesiveShots_: There is a list in `HitRollConstants.ndf` called _SuccessiveHitModifiersTable_. This parameter will yield _0_ if the target has not been hit yet, _1_ for the first successive shot and _2_ for every greater successive shot count.
- _Suppress_: Current suppress damage this unit has.

In `HitRollConstants.ndf` a developer described the dice roll calculation to be: _Success if roll > RollSuccessThreshold - modifiersum_. I interpret this to be: _Hit if random_generated_number (RNG) > RollSuccessThreshold - sum_of_every_parameter_in_HitModifierList_

If you look closely into the `HitRollConstants.ndf`, you will notice three types of dice rolls: _Hit_, _Pierce_ and _critic_:

- _Hit_: Describes the dice roll for the hit probability we just studied above.
- _Pierce_: Describes the dice roll for the probability that an kinetic AP ammunition will pierce through armor. However, there is not much else known about this dice roll for now.
- _Critic_: Describes the dice roll for the probability that this shot will trigger critical effects which will render units useless for a given time.

Currently, the only way units differ from one another is through _EBaseHitValueModifier/Idling_ and _EBaseHitValueModifier/Moving_ of _BaseHitValueModifiers_ in `Ammunition.ndf`. These values are the ones which represent the unit's _Accuracy_ reading in the armory. However, be aware that the accuracy is displayed **per salvo**. You would need to multiply these values with _NbTirParSalves_ in `Ammunition.ndf` to get the in-game displayed results.

E.g. _~/DamageTypeEvolutionOverRangeDescriptor_AP1_1Km_ points to **Distance= 175.0, AP= 1.0**. In this case the AP damage decreases **1 point every 175m**.

## Calculate Road Speed

In `UniteDescriptor.ndf` there are values called _VitesseCombat_ and _RealRoadSpeed_ which are not being used. Instead, we should use _MaxSpeed_ which represents the off-road speed. Compute (_MaxSpeed_ + _MaxSpeed_ \* _SpeedBonusOnRoad_) \* _MultiplicateurMetreRTSVersVitesseTactiquePourVehicule_ to get the true road speed.

## Calculate Autonomy

Autonomy states how far a unit can move until it runs out of fuel. In previous titles, this was measured in seconds, however, in WARNO it is specifically stated in _kilometres_. For planes, _Autonomy_ is equivalent to their _FuelMoveDuration_. For ground units, the following calculation holds very well. Be aware that this calculation was created using multiple results and searching a common pattern, hence the strange factor. Round up to the nearest integer if the first decimal place of the result is bigger than 5.

_Autonomy_ = _MaxSpeed_ \* _FuelMoveDuration_ \* _0.0000975_

## Experience & Veterancy

What experience scheme is currently being used can be seen under _ExperienceLevelsPackDescriptor_ in `UniteDescriptor.ndf`. This string is a reference to `ExperienceLevels.ndf` where all schemes are defined. However, at the moment every unit uses the following experience scheme:

- _Level 0 (POOR)_: Time in-between salves = _115%_, Precision = _-25_, Suppress Damage = _125%_
- _Level 1 (TRAINED)_: Everything at standard
- _Level 2 (VETERAN)_: Time in-between salves = _85%_, Precision = _+15_, Suppress Damage = _75%_
- _Level 3 (ELITE_: Time in-between salves = _66%_, Precision = _+25_, Suppress Damage = _50%_

Furthermore, only armed units can gain Experience (described by _CanWinExperience_).\
As outlined in `Experience.ndf`, _ExperienceGainBySecond_ and _ExperienceMultiplierBonusOnKill_ are set to 0 and 1 equivalently. This means, at least for now, units are either not able to level up or they only gain experience by killing.

## Stress, Suppression, Cohesion and Morale

**Stress** and **suppression** are one and the same variable. In-game it is called _stress_ and in the `.ndf` files it is mostly called _suppression_. Unlike Wargame: Red Dragon, this value is not shown in the WARNO UI. Instead, the current cohesion level is displayed.\
**Moral** is poorly understood. The fact that it is only non-zero for planes makes it hard to believe that it is a system that has any impact in-game, if any. It might very well be a leftover from a previous game.\
**Cohesion** is a direct effect of suppression. There are four levels which are described in `EffetsSurUnite.ndf`. Each comes with its own debuffs.

Which suppression system is being used is individually defined in `UniteDescriptor.ndf` under _SuppressDamageLevelsPack_. This variable is a reference to `DamageLevels.ndf` in which the following can be found: Every system has six different suppression levels (_calm_, _engaged_, _worried_, _stressed_, _shaken_ and (_panicked_ or _pinned_)), being triggered at different suppress damage levels defined by _Value_. Note that _Value_ is most likely only the modifier for another variable, like the maximum amount of suppression damage. Each suppression level comes with custom debuffs: Morale is being modified (_MoralModifier_), chance of hitting the target is decreased (_HitRollModifier_) and _EffectsPacks_ are being added. _EffectsPacks_ can hold multiple effects, but the most important is the cohesion being changed. Its debuffs are outlined in `EffetsSurUnite.ndf`.

Suppression damage decreases over time. The following variables describe this behavior. They can be found in `UniteDescriptor.ndf` for every unit and are all references to `DamageModules.ndf`.

- _GroundUnit_SuppressDamagesRegenRatioList_: Array detailing how much suppression damage is being recovered over a given time period: _[Time, Suppression damage recovered]_
- _GroundUnit_SuppressDamagesRegenRatioOutOfRange_: How many seconds need to pass until suppression damage recovery starts.
- _GroundUnit_MaxSuppressionDamages_: Maximum suppression damage that can be received, however, it is unknown what happens if this threshold is being exceeded.

_SuppressDamages_ in `Ammunition.ndf` describes how much suppress damage a weapon can generate. I strongly believe that the amount of suppress damage _received_ is the same for all units because _MaxSuppressionDamages_ is set to 1000 for every unit type and there is no multiplier mentioned in `UniteDescriptor.ndf` whatsoever.
