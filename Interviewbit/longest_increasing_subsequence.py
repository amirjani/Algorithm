# Find the longest increasing subsequence of a given array of integers, A.

# In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order,
# and in which the subsequence is as long as possible.

# In this case, return the length of the longest increasing subsequence.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        if n == 0:
            return 0
        lis = [1]*n
        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        return max(lis)
