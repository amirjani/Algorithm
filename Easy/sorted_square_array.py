# let's suppose we have below list
#       numbers = [1,2,3,4,5,6,7,8,9]
# new output array will be
#       output = [1,4,9,16,25,36,49,64,81]
#
# Consider what we will face if we have negative numbers in the list
#       numbers = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
# new output array will be
#      output = [1,4,9,16,25,36,49,64,81]
#
# Solution 1: O(nlogn) time | O(n) space
# Where n is the length of the input array
# and nlogn is the time complexity of the sort method
def sorted_square_array(array):
    sorted_squares = [0 for _ in array]
    for index in range(len(array)):
        value = array[index]
        sorted_squares[index] = value * value
    sorted_squares.sort()
    return sorted_squares

# Solution 2: O(n) time | O(n) space
def sorted_square_array_second_way(array):
    sorted_array = [0 for _ in array]

    left_index = 0;
    right_index = len(array) - 1;

    print("length of array is: ", len(array));
    for index in reversed(range(len(array))):
        print("index is: ", index)
        left_value = array[left_index]
        right_value = array[right_index]

        if abs(left_value) > abs(right_value):
            sorted_array[index] = left_value * left_value
            left_index += 1
        else:
            sorted_array[index] = right_value * right_value
            right_index -= 1

    return sorted_array;

numbers = [1,2,3,4,5,6,7,8,9]
squared_numbers = sorted_square_array(numbers)
print(squared_numbers)

numbers = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]
squared_numbers = sorted_square_array_second_way(numbers)
print(squared_numbers)
