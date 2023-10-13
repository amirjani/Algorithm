# N children are standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.

# Children with a higher rating get more candies than their neighbors.
# What is the minimum number of candies you must give?

# Example Input:  A = [1, 5, 2, 1]
# Output: 7
class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        if n == 1:
            return 1
        candies = [1]*n
        for i in range(1, n):
            if A[i] > A[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)
