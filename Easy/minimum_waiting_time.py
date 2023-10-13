# Description:
# You're given a non-empty array of positive integers representing the amounts
# of time that specific queries take to execute. Only one query can be executed
# at a time, but the queries can be executed in any order.
#
# A query's waiting time is defined as the amount of time that it must wait
# before its execution starts. In other words, if a query is executed second,
# then its waiting time is the duration of the first query; if a query is
# executed third, then its waiting time is the sum of the durations of the
# first two queries.

# Write a function that returns the minimum amount of total waiting time for all
# Example Input: [3,2,1,2,6]
# Example Output: 17
def minimum_waiting_time(numbers):
    numbers.sort()
    waiting_time = 0

    for index, duration in enumerate(numbers):
        # why enumerate? because we need to know the index of the number
        # why index+1? because we need to know the number of queries that have already been executed
        # why len(numbers) - (index+1)? because we need to know the number of queries that have not been executed
        numbers_left = len(numbers) - (index+1)
        # why duration * numbers_left? because we need to know the total waiting time for the current query
        waiting_time += duration * numbers_left

    return waiting_time


array_of_numbers = [3, 2, 1, 2, 6]
print(minimum_waiting_time(array_of_numbers))
