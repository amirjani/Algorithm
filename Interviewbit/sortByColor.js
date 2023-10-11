/**
  Given an array with N objects colored red, white, or blue,
  sort them so that objects of the same color are adjacent,
  with the colors in the order red, white, and blue.

  We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.
*/

module.exports = {
 //param A : array of integers
 //return a array of integers
	sortColors : function(colors){
	  var redCount = 0;
    var whiteCount = 0;
    var blueCount = 0;

    // first pass to count colors
    for(var i = 0; i < colors.length; i++){
      if(colors[i] === 0){
        redCount++;
      }
      if(colors[i] === 1){
        whiteCount++;
      }
      if(colors[i] === 2){
        blueCount++;
      }
    }

    var sorted = [];
    for(var i = 0; i < redCount; i++){
      sorted.push(0);
    }
    for(var i = 0; i < whiteCount; i++){
      sorted.push(1);
    }
    for(var i = 0; i < blueCount; i++){
      sorted.push(2);
    }
    return sorted;
	}
};


sortColors([0, 1, 2, 0, 1, 2]); // [0, 0, 1, 1, 2, 2]
