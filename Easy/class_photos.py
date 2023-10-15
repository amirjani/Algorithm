# Description
# You are given two arrays, one containing the heights of all students with red
# shirts and another one containing the heights of all students with blue shirts.
# These arrays will always have the same length, and each height will be a
# positive integer. Write a function that returns whether or not a class photo
# that follows the stated guidelines can be taken.
#
# Note: you can assume that each class has at least 2 students.
#
# Sample Input
# redShirtHeights = [5, 8, 1, 3, 4]
# blueShirtHeights = [6, 9, 2, 4, 5]
# Sample Output
# true
def class_photos(red_shirt_heights, blue_shirt_heights):
    # First we sort the arrays in descending order so that we can compare the
    # tallest students from each class
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    # Then we check if the tallest student from each class is the same height
    # If they are, then we return False because we can't take a class photo
    if red_shirt_heights[0] == blue_shirt_heights[0]:
        return False

    # Then we check if the tallest student from the red shirt class is taller
    if red_shirt_heights[0] > blue_shirt_heights[0]:
        # Then we iterate through the arrays and check if the red shirt students
        # are taller than the blue shirt students
        for index, height in enumerate(red_shirt_heights):
            if height <= blue_shirt_heights[index]:
                return False
    else:
        for index, height in enumerate(blue_shirt_heights):
            if height <= red_shirt_heights[index]:
                return False

    return True


# Time Complexity: O(nlog(n)) -> because we have to sort the arrays
# Space Complexity: O(1) -> because we don't use any extra space
print(class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
