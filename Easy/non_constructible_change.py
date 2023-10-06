# Description:
    # Given an array of positive integers representing the values of coins in your possession,
    # write a function that returns the minimum amount of change (the minimum sum of money)
    # that you cannot create. The given coins can have any positive integer value and aren't necessarily unique
    #
    # For example, if you're given coins = [1,2,5], the minimum amount of change that you can't create is 4.
    # If you're given no coins, the minimum amount of change that you can't create is 1.
    #
    # Sample Input:
        # coins = [5,7,1,1,2,3,22]
        # output = 20
        #
        # coins = [1,2,3,4,5,6,7,8,9]
        # output = 46
        #
        # coins = [1,2,5]
        # output = 4

coins = [1,2,5]

# Solution 1: O(nlogn) time | O(1) space
# Where n is the length of the input array
# and nlogn is the time complexity of the sort method
def non_constructible_change(coins):
    coins.sort()
    current_change_created = 0

    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin

    return current_change_created + 1


print(non_constructible_change(coins))
