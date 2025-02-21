//Given a string s, find the length of the longest
// substring without duplicate characters.

// Example:
// Input: s = "abcabcbb"
// output: 3
// Explanation: The answer is "abc", with the length of 3.


function lengthOfLongestSubstring(givenString: string): number {
    const possibleSubstring: Map<string, number> = new Map();

    // Initialize pointers and max length
    let start: number = 0;
    let end: number = 0;
    let max: number = 0;

    // Edge case for single character string
    if (givenString.length === 1) return 1;

    while (start <= end && end < givenString.length) {
        const currentChar: string = givenString[end];

        if (possibleSubstring.has(currentChar)) {
            const prevPosition: number = possibleSubstring.get(currentChar)!;

            if (prevPosition >= start) {
                // Move start pointer to position after previous occurrence
                start = prevPosition + 1;
            } else {
                // Update max if current window is larger
                max = Math.max(end - start + 1, max);
            }

            // Update character position
            possibleSubstring.set(currentChar, end);
        } else {
            // New character found
            possibleSubstring.set(currentChar, end);

            max = Math.max(end - start + 1, max);
        }
        end++;

        console.log("possibleSubstring", possibleSubstring, start, end, max)
    }

    return max;
}

const res = lengthOfLongestSubstring("abcabcbb");
  console.log("res: ", res);