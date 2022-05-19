### About WARNO
WARNO is the newest addition to the French studio [Eugen Systems'](https://eugensystems.com/) glorious range of real time tactics games. It is currently available as Early Access on [Steam](https://store.steampowered.com/app/1611600/WARNO/). As the spiritual successor to the acclaimed *Wargame* series, WARNO is the ultimate next-gen World War III battle simulator, boasting hundreds of the Cold War-era's most legendary units from NATO and the Warsaw Pact.

One of the game's draws is its fine-grained level of combat simulation. You will be building "decks" of units based on a multitude of different stats displayed on its unit "card": From road speed over supply cost to armored-piercing capabilities, just to name a few.

Unfortunately, you will eventually come to the realization that these cards withhold much important information and crucial characteristics. Heck, they even display inaccuracies frequently. Here at **WARNO-DATE** we are determined to change exactly that:

### The Goal of This Project
* Provide easy readable ***.csv*** (comma-separated values) files of the important data files like *UniteDescriptor.ndf*, *WeaponDescriptor.ndf* and many more. Import of the csv-format is natively supported by applications like Excel and MySQL Workbench.
* ***SQL query templates*** in order to simply create tables for these before created .csv files.
* ***Guide*** on how to adjust the python data exporter scripts to support further .ndf files.
* ***Wiki*** containing a dictionary which explains every important data variable and a documentation for the most crucial game mechanics like accuracy, damage calculation and many more.
* Unlimited and free of charge ***API*** where everyone will be able to receive data on units over the internet via the industry standard data interchange format ***.json***.

### Official Wiki
This project's own official wiki is hosted here on [GitHub](https://github.com/BE3dARt/WARNO-DATA/wiki). Use the following table of content to navigate its various subsections.

[Data Dictionary](https://github.com/BE3dARt/WARNO-DATA/wiki/Data-Dictionary)\
This chapter maintains a dictionary which states and explains the most important variables of the most used .ndf game files like UniteDescriptor.ndf, WeaponDescriptor.ndf and many more. 

[In Depth-Guide to Game Mechanics](https://github.com/BE3dARt/WARNO-DATA/wiki/In-Depth-Guide)\
Holds relevant game mechanics like accuracy, damage calculation, just to name a few.

[Getting the Data](https://github.com/BE3dARt/WARNO-DATA/wiki/Getting-the-Data)\
A tutorial on how to download and further process the exported .csv configuration files.

[Python Data Exporter](https://github.com/BE3dARt/WARNO-DATA/wiki/Python-Data-Exporter)\
Although each python script is commented, this chapter will guide you through various parts of the python exporter; structure, requirements, how to run it and what needs to be changed in order to add new files to the extractor.

### Word of Thanks
I wanted to thank the following beautiful people and the whole WARNO community on [Discord](https://discord.gg/ruDBq9SFB4). Without them, this project would have gone nowhere:
* **eMeM** for the *calculation of road speed*, a guess on *recource tickets*, help with *experience & veterancy* and the discussion over *stress, suppression, cohesion and morale* and *damage calculation*.
* **unipus** for pointing me towards the right direction in *AP damage for kinetic weapons*.
* **gagarin** for helping me finding the variable causing *filter by category* in the in-game armory.
* **Iris** for helping me getting in-game displayed *accuracy* right.
* **Terminus Est** for defining *Salves* and *SalvoStockIndex* in WeaponDescriptor.ndf and having a discussion with me about the accuracy and damage calculation.
* **swizzlewizzle** for having a discussion with me about the damage calculation.

### Copyright Notice
Each and every bit of the gathered data belongs to [Eugen Systems](https://eugensystems.com/). This project will always be free of charge and dedicated to serve the awesome WARNO community.