# Description:
# You're given two non-empty arrays of positive integers. One array represents
#

red_shift_speeds = [5, 5, 3, 9, 2]
blue_shift_speeds = [3, 6, 7, 2, 1]
fastest = True


def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort()

    if fastest:
        blue_shirt_speeds.reverse()

    total_speed = 0

    for index, speed in enumerate(red_shirt_speeds):
        total_speed += max(speed, blue_shirt_speeds[index])

    return total_speed


print(tandem_bicycle(red_shift_speeds, blue_shift_speeds, fastest))
