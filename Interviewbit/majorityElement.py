class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        if len(A) == 1:
            return A[0]
        majority_element = A[0]
        majority_element_count = 1
        for i in range(1, len(A)):
            if A[i] == majority_element:
                majority_element_count += 1
            else:
                majority_element_count -= 1
                if majority_element_count == 0:
                    majority_element = A[i]
                    majority_element_count = 1
        return majority_element
