def tandemBicycle(red_shirt_speeds: list, blue_shirt_speeds: list, fastest: bool):
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort(reverse=fastest)
    total_speed = 0
    for index, temp in enumerate(red_shirt_speeds):
        total_speed += max(red_shirt_speeds[index], blue_shirt_speeds[index])
    return total_speed


class TandemBicycle:
    red_shirt_speeds = list(map(int, input().split()))
    blue_shirt_speeds = list(map(int, input().split()))
    fastest = bool(input())
    print(tandemBicycle(red_shirt_speeds, blue_shirt_speeds, fastest))
