# Given a string A, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        max_length = 0
        current_length = 0
        current_substring = ""
        for i in range(len(A)):
            print("A: ", i, A[i])
            if A[i] not in current_substring:
                print("current_substring: ", current_substring)
                current_substring += A[i]
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                current_substring = A[i]
                current_length = 1
        if current_length > max_length:
            max_length = current_length
        return max_length


if __name__ == "__main__":
    solution = Solution()
    # print(solution.lengthOfLongestSubstring("abcabcbb"))
    # print(solution.lengthOfLongestSubstring("bbbbb"))
    # print(solution.lengthOfLongestSubstring("pwwkew"))
    print("value is : ", "dadbc")
    print(solution.lengthOfLongestSubstring("daDbc"))
