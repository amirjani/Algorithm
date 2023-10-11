# Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left = 0
        right = 0
        max_len = 0
        zero_count = 0

        while right < len(A):
            if A[right] == 0:
                zero_count += 1

            while zero_count > B:
                if A[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
