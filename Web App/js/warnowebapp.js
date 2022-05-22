///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Global Variables
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
var specificationIterator = 0; //Iterate over every specification
var exp = 0.85; //The exponent which is used to build the 'weight-curve'

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Generate the 'weight-curve'
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function getWeights(number, exponent, index) {
	
	var outPutArray = [];
	var spacing = 1/(number + 1);
	var sum = 0;
	
	//Weight berechnen und in Array eintragen
	for (let i = number; i > 0; i--) {
		outPutArray.push(Math.pow(spacing*(i),exponent)); //Append array entry
		sum += Math.pow(spacing*(i),exponent);
    }
	
	//Adjust for range(0 to 1)
	for (let i = 0; i < outPutArray.length; i++) {
		outPutArray[i] = outPutArray[i] / sum;
    }
	
	return outPutArray[index];
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Find the winner - Analyse the generated array and choose the winner based on calculated ratings
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function findWinner() {

	//Add the values of all specifications to find the winner
  var iterator = 0;
  
  while (wargameUnits[0][2][iterator] != null) {
  	for (let i = 1; i < wargameUnits.length; i++) {
		wargameUnits[0][2][iterator][1] = wargameUnits[0][2][iterator][1] + wargameUnits[i][2][iterator][1]
	}
	iterator += 1;
  }
  
  //Sort in descending order
  wargameUnits[0][2].sort((a,b) => a[1] - b[1]);
  wargameUnits[0][2].reverse();
  
  specificationIterator = 0;
  
  console.log(wargameUnits[0][2]);
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// API Handle - Call the API and return an array with the unit's name and the corresponding rating
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const request = async (specification, weight, condition, mode, order) => {

    //Form fetch URL
    var url = "https://api.be3dart.ch/wargame-red-dragon.php?specification=Name, " + specification + "&condition=" + condition +  "&order=" + order +"&arrangement=desc";;

    //1. Get the data from the API
    const response = await fetch(url);

    //2. Format the received data into JSON
    const result = await response.json();
	
	//Find 'max' and 'min' of 'specification'
	var max = result[0][specification];
	var min = result[0][specification];
	for (let i = 0; i < result.length; i++) {
		if (parseInt(result[i][specification]) > max) {
			max = parseInt(result[i][specification]);
		} else if (parseInt(result[i][specification]) < min) {
			min = parseInt(result[i][specification]);
		}
	}
	
	//If reversed, exchange variables
	if (mode != 0) {
		[max, min] = [min, max];
	} 
	
    //Loop over every entry in JSON and calcualte it's value
    let test = [];
    for (let i = 0; i < result.length; i++) {
      test.push([]); //Append array entry
      test[i][0] = result[i].Name //Fill in unit name
	  test[i][1] = Math.abs((parseInt(result[i][specification]) - min)/(max-min)) * weight;
	  //console.log("Name: " + test[i][0] + ", Value: " + test[i][1]);
    }
	
    return test;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Prepare API Request - Handles calls to async 'request' and go on with program when every specification is done
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function rolling(condition) {
  request(wargameUnits[specificationIterator][0], getWeights(wargameUnits.length, 0.85, specificationIterator), condition, wargameUnits[specificationIterator][3], wargameUnits[0][0]).then(evaluatedArray => {

	wargameUnits[specificationIterator][2] = evaluatedArray;
	
    wargameUnits[specificationIterator][1] = true;
    specificationIterator += 1;

    for (let i = 0; i < wargameUnits.length; i++) {
      if (wargameUnits[i][1]==false) {
        rolling(condition);
		break;
      }
    }

    if (wargameUnits.every(function (e) {return e[1] == true}) == true) {
      findWinner();
    }
  });
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Start
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function start () {

  var tempString = "";

  //Settings to String
  for (let i = 0; i < wargameSettings.length; i++) {
    tempString = tempString + wargameSettings[i] + " and ";
  }

  //Mother country to String
  tempString = tempString + "(";
  for (let i = 0; i < wargameCountry.length; i++) {
    tempString = tempString + wargameCountry[i] + " or ";
  }
  tempString = tempString.slice(0, -4);
  tempString = tempString + ")";
	
  //Start recursive function
  rolling(tempString);
}
//start();