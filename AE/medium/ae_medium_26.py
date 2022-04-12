def get_next(current: int, array: list) -> int:
    offset = array[current]
    return ((current + offset) % len(array)) if offset >= 0 else ((current - abs(offset)) % len(array))


def hasSingleCycle(array: list) -> bool:
    current, visited_elements = 0, 0
    while visited_elements < len(array):
        if visited_elements > 0 and current == 0:
            return False
        visited_elements += 1
        current = get_next(current, array)
    return current == 0


class SingleCycleCheck:
    input = list(map(int, input().split()))
    print(hasSingleCycle(input))
