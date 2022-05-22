import collections


class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.time_map.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= values[mid][1]:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result


class TimeBasedKeyValueStore:
    time_map = TimeMap()
    time_map.set("abc", "123", 7)
    print(time_map.get("def", 10))
