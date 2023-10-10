/**
    https://www.interviewbit.com/problems/colorful-number/
 
    For Given Number number, find if it's a COLORFUL number or not.

        COLORFUL number:
        number number can be broken into different contiguous sub-subsequence parts. 
        Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
        And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
        Return 1 if number is a COLORFUL number, else return 0
 */

module.exports = { 
    //param number : integer
    //return an integer
    colorful : function(number){
        var map = {};
        var digits = number.toString().split('');
        for(var i = 0; i < digits.length; i++){
            var product = 1;
            for(var j = i; j < digits.length; j++){
                product *= digits[j];
                if(map[product] != null){
                    return 0;
                }
                map[product] = true;
            }
        }
        return 1;
    }
};
           