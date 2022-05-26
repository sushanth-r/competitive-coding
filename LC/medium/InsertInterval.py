from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        if not intervals:
            return [new_interval]
        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                result.append(new_interval)
                return result + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        result.append(new_interval)
        return result


class InsertInterval:
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    x = Solution().insert(intervals, newInterval)
    print(x)
