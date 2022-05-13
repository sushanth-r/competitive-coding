from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p, s) for p, s in (zip(position, speed))]
    time_stack = []
    for p, s in sorted(pair, key=lambda x: x[0])[::-1]:
        distance_to_cover = target - p
        time_to_cover = distance_to_cover / s
        time_stack.append(time_to_cover)
        if time_stack and len(time_stack) >= 2:
            if time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
    return len(time_stack)


class CarFleet:
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    target = int(input())
    print(carFleet(target, position, speed))
