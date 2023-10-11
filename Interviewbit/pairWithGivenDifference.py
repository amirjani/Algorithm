# Given an one-dimensional unsorted array A containing N integers.
# You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
# Return 1 if any such pair exists else return 0.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        print(A)

        left_index = 0
        right_index = 1

        while left_index < len(A) and right_index < len(A):
            if A[right_index] - A[left_index] == B:
                return 1
            elif A[right_index] - A[left_index] < B:
                right_index += 1
            else:
                left_index += 1

        return 0
