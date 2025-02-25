// You are given a sorted unique integer array nums.
// A range [a,b] is the set of all integers from a to b (inclusive).

// Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of
// nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

function summaryRanges(numbers: number[]): string[] {
    let currentSmallestNumber = numbers[0];
    let currentString = '';

    let finalString: string[] = [];

    for (let i = 1; i <= numbers.length; i++) {
        if (numbers[i] - numbers[i-1] === 1) continue;

        console.log("numbers[i-1]: ", numbers[i-1], "i: ", i, "currentSmallestNumber: ", currentSmallestNumber);
        if (currentSmallestNumber === numbers[i-1]) {
            currentString = `${currentSmallestNumber}`
        } else {
            currentString = `${currentSmallestNumber}->${numbers[i-1]}`
        }

        finalString.push(currentString);
        currentSmallestNumber = numbers[i];
    }

    return finalString;
}

summaryRanges([0,1,2,4,5,7]);