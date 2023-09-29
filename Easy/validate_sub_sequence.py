# sub sequence ->
#   a sequence that can be derived from another sequence by deleting some or no elements
#   without changing the order of the remaining elements
#
# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
#
# A single number in an array and the array itself are both valid subsequences of the array.

# Sample Input:
    # array = [5, 1, 22, 25, 6, -1, 8, 10]
    # sequence = [1, 6, -1, 10]
    # output = true
    #
    # array = [5, 1, 22, 25, 6, -1, 8, 10]
    # sequence = [5, 1, 22, 25, 6, -1, 8, 10]
    # output = true

# Solution 1: O(n) time | O(1) space
# Where n is the length of the sequence array
def validate_sub_sequence(sequence, potential_sub_sequence):
    sequence_index = 0
    sub_sequence_index = 0
    while sequence_index < len(sequence) and sub_sequence_index < len(potential_sub_sequence):
        if sequence[sequence_index] == potential_sub_sequence[sub_sequence_index]:
            sub_sequence_index += 1
        sequence_index += 1
    return sub_sequence_index == len(potential_sub_sequence)

def validate_sub_sequence_with_for_loop(sequence, potential_sub_sequence):
    sequence_index = 0;
    for number in sequence:
        if sequence_index == len(potential_sub_sequence):
            break
        if number == potential_sub_sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(potential_sub_sequence)

sequence = [5, 1, 22, 25, 6, -1, 8, 10]
potential_sub_sequence = [1, 6, -1, 10]

# check time complexity
is_sequence_sub = validate_sub_sequence(sequence, potential_sub_sequence);
print(is_sequence_sub)

is_sequence_sub = validate_sub_sequence_with_for_loop(sequence, potential_sub_sequence);
print(is_sequence_sub)
