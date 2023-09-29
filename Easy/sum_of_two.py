# Consider we have below Numbers and a target number
# Numbers = [3,5,-4,8,11,1,-1,6], target = 10
# Find the pair of numbers from the list which sums to the target number
# In this case, the pair is 1,9 and 2,8 and 3,7 and 4,6
# If there is no pair, print "No Pair Found"


numbers = [3,5,-4,8,11,1,-1,6]
target_sum = 10

# Two four loops 
# First Way
# * Time Complexity is O(n^2)
# * Space Complexity is O(1) -> No extra space is used
def sum_of_two(numbers, target_sum):
    for numbersIndex in range(len(numbers) - 1):
        currentNumber = numbers[numbersIndex]
        for j in range(numbersIndex+1, len(numbers)): 
            afterNumber = numbers[j]
            if (currentNumber + afterNumber == target_sum):
                return [currentNumber, afterNumber]
    return[];

# Second Way
# Using Hash Table
# * Time Complexity is O(n) -> N is the length of the list
# * Space Complexity is O(n) -> N is the length of the list
# target_sum=10
# current_number=x
# y=target_sum-x
# let's consider x is 3, then y must be 7
# if we have y in the list, then we have a pair
def sum_of_two_with_hash(numbers, target_sum): 
    nums = {}
    for num in numbers: 
        potentialMatch = target_sum - num
        if potentialMatch in nums: 
            return [potentialMatch, num]
        else: 
            nums[num] = True
    return[]

# Third way 
# First sort the list -> O(nlogn)
def sum_of_two_with_sort(numbers, target_sum):
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right: 
        current_sum = numbers[left] + numbers[right]
        if current_sum == target_sum: 
            return [numbers[left], numbers[right]]
        elif current_sum < target_sum: 
            left += 1
        elif current_sum > target_sum: 
            right -= 1
    return[]
