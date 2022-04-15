def sunsetViews(buildings: list, direction: str):
    result = []
    if direction == "EAST":
        buildings.reverse()
    tallest_building = float("-inf")
    for i in range(len(buildings)):
        if buildings[i] > tallest_building:
            tallest_building = buildings[i]
            result.append(i)
    if direction == "EAST":
        result = list(map(lambda x: ((len(buildings) - 1) - x), result))
        result.reverse()
    return result


class SunsetViews:
    buildings = list(map(int, input().split()))
    direction = input()
    print(sunsetViews(buildings, direction))
