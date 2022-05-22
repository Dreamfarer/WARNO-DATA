//https://github.com/ResidentMario/wargame-data
var options = [
[
	["Armor (Front)", "ArmorFront", 0, true],
	["Armor (Side)", "ArmorSides", 0, true],
	["Armor (Top)", "ArmorTop", 0, true],
	["Armor (Rear)", "ArmorRear", 0, true],
	["ECM", "ECM", 0, true],
	["Size", "SizeModifier", 0, true],
	["Strength", "Strength", 0, true],
	["Deployable Amount (Rookie)", "RookieDeployableAmount", 0, true],
	["Deployable Amount (Trained)", "TrainedDeployableAmount", 0, true],
	["Deployable Amount (Hardened)", "HardenedDeployableAmount", 0, true],
	["Deployable Amount (Veteran)", "VeteranDeployableAmount", 0, true],
	["Deployable Amount (Elite)", "EliteDeployableAmount", 0, true],
	["Cards", "MaxPacks", 0, true],
	["Price", "Price", 1, true],
	["Production Time", "ProductionTime", 0, true],
	["Fuel Capacity", "FuelCapacity", 0, true],
	["Autonomy", "Autonomy", 0, true],
	["Acceleration", "MaxAcceleration", 0, true],
	["Deceleration", "MaxDeceleration", 0, true],
	["Speed", "MaxSpeed", 0, true],
	["Year", "Year", 0, true],
	["Turn Speed", "TimeHalfTurn", 0, true],
	["Altitude (Airplane)", "AirplaneFlyingAltitude", 0, true],
	["Manoeuvrability (Helicopter)", "CyclicManoeuvrability", 0, true],
	["Lateral Speed (Helicopter)", "LateralSpeed", 0, true],
	["Detection (Air to Air)", "AirToAirHelicopterDetectionRadius", 0, true],
	["Detection (Helicopter)", "HelicopterDetectionRadius", 0, true],
	["Detection (Groud to Air)", "OpticalStrengthAir", 0, true],
	["Detection (Groud to Ground)", "OpticalStrengthGround", 0, true],
	["Detection (SEAD)", "OpticalStrengthAntiradar", 0, true],
	["Stealth", "Stealth", 0, true],
	["Supply Capacity", "SupplyCapacity", 0, true]
],

[
	["HE Splash Resistant (Front)", "ArmorFrontSplashResistant", 0],
	["HE Splash Resistant (Side)", "ArmorSidesSplashResistant", 0],
	["HE Splash Resistant (Top)", "ArmorTopSplashResistant", 0],
	["HE Splash Resistant (Rear)", "ArmorRearSplashResistant", 0],
	["Command Unit", "IsCommandUnit", 0],
	["Prototype", "IsPrototype", 0],
	["Transporter", "IsTransporter", 0],
	["Amphibious", "Amphibious", 0]
],

[
	["Deck", "Deck", true],
	["Ship Type", "Sailing", true],
],

[
	["United States", "United States", "MotherCountry", true],
	["France", "France", "MotherCountry", true],
	["United Kingdom", "United Kingdom", "MotherCountry", true],
	["Federal Republic of Germany", "West Germany", "MotherCountry", true],
	["Canada", "Canada", "MotherCountry", true],
	["Denmark", "Denmark", "MotherCountry", true],
	["Norway", "Norway", "MotherCountry", true],
	["Netherlands", "The Netherlands", "MotherCountry", true],
	["Sweden", "Sweden", "MotherCountry", true],
	["Japan", "Japan", "MotherCountry", true],
	["South Korea", "South Korea", "MotherCountry", true],
	["Australian and New Zealand Army Corps", "ANZAC", "MotherCountry", true],
	["Israel", "Israel", "MotherCountry", true],
	["South Africa", "South Africa", "MotherCountry", true],
	["Soviet Union", "Soviet Union", "MotherCountry", true],
	["German Democratic Republic", "East Germany", "MotherCountry", true],
	["Poland", "Poland", "MotherCountry", true],
	["Czechoslovakia", "Czechoslavakia", "MotherCountry", true],
	["China", "China", "MotherCountry", true],
	["North Korea", "North Korea", "MotherCountry", true],
	["Yugoslavia", "Yugoslavia", "MotherCountry", true],
	["Finland", "Finland", "MotherCountry", true]
],

[

	["Helicopter", "HEL", "Tab", true],
	["Infantry", "INF", "Tab", true],
	["Logistic", "LOG", "Tab", true],
	["Planes", "PLA", "Tab", true],
	["Reconaissance", "REC", "Tab", true],
	["Ship", "SHP", "Tab", true],
	["Support", "SUP", "Tab", true],
	["Tank", "TNK", "Tab", true],
	["Vehicle", "VHC", "Tab", true]

]

];

var wargameData = [[], [], []]; //[0]: Unit, [1]: Nation, [2]: Condition
var colors = ["#00e060", "#ffffff", "#e21515"]; //[0]: True, [1]: Not active, [2]: False

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Create HTML table to display nations
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function createTable (rows, table, index) {

	var tempString = "";
	var counter = 1;
	for (iterator = 0; iterator < options[index].length; iterator++) {

		if (counter == 1) {
			tempString += "<tr>" + "<td onclick=\"clickEvent(" + index + ", " + iterator + ")\" name=\"" + options[index][iterator][0] + "\">" + options[index][iterator][0] + "</td>";
		} else if (counter > 1 && counter < rows) {
			tempString += "<td onclick=\"clickEvent(" + index + ", " + iterator + ")\" name=\"" + options[index][iterator][0] + "\">" + options[index][iterator][0] + "</td>";
		} else if (counter == rows) {
			tempString += "<td onclick=\"clickEvent(" + index + ", " + iterator + ")\" name=\"" + options[index][iterator][0] + "\">" + options[index][iterator][0] + "</td>" + "</tr>";
			counter = 0;
		}
		counter += 1;
	}

	table.innerHTML = tempString;

}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function called when a specification is being deactivated
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function removeActive(index, iterator) {

	//HTML
	
	if (index == 0) {
		
		//Number
		document.getElementsByName(options[index][iterator][0])[0].remove();
		document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[1];
		
	} else if (index == 3 || index == 4 || index == 1) {
		
		//Condition
		document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[1];
		
	} 
	
	//Keep track of button-state
	if (index == 1) {
		
		//More than 2 button states
		options[index][iterator][(options[index][iterator].length - 1)] = 0;
		
	} else {
		
		//Boolean
		options[index][iterator][(options[index][iterator].length - 1)] = true;
	}
	
	//Javascript
	if (index == 0) {
		
		//Number
		var iteratorNest = 0;
		while (wargameData[0][iteratorNest] != null) {

			if (wargameData[0][iteratorNest][0] == options[index][iterator][1]) {
				wargameData[0].splice(iteratorNest, 1);
				break;
			}
			iteratorNest += 1;
		}
		
	} else if (index == 3) {
		
		//Condition (Country)
		var iteratorNest = 0;
		while (wargameData[1][iteratorNest] != null) {

			if (wargameData[1][iteratorNest] == options[index][iterator][2] + "='" + options[index][iterator][1] + "'") {
				wargameData[1].splice(iteratorNest, 1);
				break;
			}
			iteratorNest += 1;
		}
		
	} else if (index == 4) {
		
		//Condition (Settings) (String)
		var iteratorNest = 0;
		while (wargameData[2][iteratorNest] != null) {

			if (wargameData[2][iteratorNest] == options[index][iterator][2] + "='" + options[index][iterator][1] + "'") {
				wargameData[2].splice(iteratorNest, 1);
				break;
			}
			iteratorNest += 1;
		}
	} else if (index == 1) {
		
		//Condition (Settings) (Boolean)
		var iteratorNest = 0;
		while (wargameData[2][iteratorNest] != null) {

			if (wargameData[2][iteratorNest] == options[index][iterator][1] + "=" + "false") {
				wargameData[2].splice(iteratorNest, 1);
				break;
			}
			iteratorNest += 1;
		}
		
	}
	
	searchEvent(); //Update listing
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function called when a specification is chosen
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function addActive(index, iterator) {
	
	//Change HTML
	if (index == 0) {
		
		//'Search'-Menu
		document.getElementById("selection").innerHTML += "<li class=\"text-white\" name=\"" + options[index][iterator][0] + "\" onclick='removeActive(" + index + ", " + iterator + ")'>" + options[index][iterator][0] + "</li>";
		document.getElementsByName(options[index][iterator][0])[1].style.backgroundColor = colors[0];
		
	} else if (index == 3) {
		
		//Buttons
		document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[0];
		
	} else if (index == 4) {
		
		//Buttons (Only 1 active at any given time)
		for (i = 0; i < options[index].length; i++) {
			
			if (options[index][i][(options[index][i].length - 1)] == false) {
				removeActive(index, i); //Remove any active buttons first
			}
		}
		document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[0];
		
	} else if (index == 1) {
		
		//Buttons (Multiple States)
		if (options[index][iterator][(options[index][iterator].length - 1)] + 1 == 1) {
			document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[0];
		} else if (options[index][iterator][(options[index][iterator].length - 1)] + 1 == 2) {
			document.getElementsByName(options[index][iterator][0])[0].style.backgroundColor = colors[2];
		}
		
	}
	
	//Keep track of button-state
	if (index == 1) {
		
		//More than 2 button states
		options[index][iterator][(options[index][iterator].length - 1)] += 1;
		
	} else {
		
		//Boolean
		options[index][iterator][(options[index][iterator].length - 1)] = false;
	}

	//Change Javascript
	if (index == 0) {
		
		//Number
		wargameData[0].push([[],false,[],[]]); //Add new item
		wargameData[0][wargameData[0].length-1][0] = options[index][iterator][1];
		wargameData[0][wargameData[0].length-1][3] = options[index][iterator][2];
		
	} else if (index == 3) {
		
		//Condition (Country)
		wargameData[1].push([]);
		wargameData[1][wargameData[1].length-1] = options[index][iterator][2] + "='" + options[index][iterator][1] + "'";
	
	} else if (index == 4) {
		
		//Condition (String)
		wargameData[2].push([]);
		wargameData[2][wargameData[2].length-1] = options[index][iterator][2] + "='" + options[index][iterator][1] + "'";
		
	} else if (index == 1) {
		
		//Condition (Boolean)
		if (options[index][iterator][(options[index][iterator].length - 1)] == 1) {
			
			//Add as we normally would. Only 3rd state (below) is different
			wargameData[2].push([]);
			wargameData[2][wargameData[2].length-1] = options[index][iterator][1] + "=" + "true";
			
		} else {
			
			//We need to find the index of the specification first in order to change it's value
			var iteratorNest = 0;
			while (wargameData[2][iteratorNest] != null) {

				if (wargameData[2][iteratorNest] == options[index][iterator][1] + "=" + "true") {
					wargameData[2][iteratorNest] = options[index][iterator][1] + "=" + "false";
					break;
				}
				iteratorNest += 1;
			}
			
			
		}
		
	}
	
	searchEvent(); //Update listing
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fire when 'search' is used
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function searchEvent() {

	var input, filter, ul, li; //Define variables

	input = document.getElementById("mySearch"); //Reference to element
	filter = input.value.toUpperCase(); //Convert to uppercase to match

	ul = document.getElementById("myMenu");

	ul.innerHTML = "";

	if (filter.length >= 1) {

		for (i = 0; i < options.length; i++) {

			//Applies only to the 0th index of 'options'
			if (i == 0 || i == 3) {

				var iterator  = 0;
				while (options[i][iterator] != null) {

					if (options[i][iterator][0].toUpperCase().includes(filter) && options[i][iterator][(options[i][iterator].length - 1)] == true) {
						ul.innerHTML += "<a onclick='addActive(" + i + ", " + iterator + ")'>" + options[i][iterator][0] + "</a>";
					}
					iterator += 1;
				}
			}
		}
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fire when a button on a table is pressed
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function clickEvent(index, iterator) {
	
	
	if (index == 1) {
		
		//Multi-state buttons
		if (options[index][iterator][(options[index][iterator].length - 1)] != 2) {
			addActive(index, iterator);
		} else {
			removeActive(index, iterator);
		}
		
	} else {
		
		//Boolean buttons
		if (options[index][iterator][(options[index][iterator].length - 1)] == true) {
			addActive(index, iterator);
		} else {
			removeActive(index, iterator);
		}
		
	}
	
	//Decide when to open the sidebar
	if (wargameData[0][0] == null && wargameData[1][0] == null && wargameData[2][0] == null) {
		closeNav();
	} else {
		openNav();
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill in pre-defined tables
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
createTable(4, 	document.getElementById("tableNation"), 3);
createTable(4, 	document.getElementById("tableTab"), 4);
createTable(4, 	document.getElementById("tableSpecifications"), 1);
createTable(4, 	document.getElementById("tableCalculations"), 0);