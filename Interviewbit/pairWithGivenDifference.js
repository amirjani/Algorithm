/**
  Given an one-dimensional unsorted array A containing N integers.

  You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

  Return 1 if any such pair exists else return 0.
*/

module.exports = {
 //param A : array of integers
 //param B : integer
 //return an integer
	solve : function(numbers, pairToBeFound){

	   var sorted = numbers.sort(function(a, b){
        return a - b;
      });

      var left = 0;
      var right = 1;
      while(left < sorted.length && right < sorted.length){
        var difference = sorted[right] - sorted[left];
        if(difference === pairToBeFound && left !== right){
          return 1;
        }
        if(difference < pairToBeFound){
          right++;
        }
        if(difference > pairToBeFound){
          left++;
        }
      }
      return 0;
	}
};
