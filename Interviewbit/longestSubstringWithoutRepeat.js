// https://www.interviewbit.com/problems/longest-substring-without-repeat/

module.exports = { 
     //param word : string
     //return an integer
     lengthOfLongestSubstring : function(word){
          var map = {};
          var max = 0;
          var start = 0;
          for(var wordIndex = 0; wordIndex < word.length; wordIndex++){
               var current = word[wordIndex];
               if(map[current] != null){
                    max = Math.max(max, wordIndex - start);
                    for(var j = start; j < map[current]; j++){
                         delete map[word[j]];
                    }
                    start = map[current] + 1;
               }
               map[current] = wordIndex;
          }
          return Math.max(max, word.length - start);
       }
   };
   