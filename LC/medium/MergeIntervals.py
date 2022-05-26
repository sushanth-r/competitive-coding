from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]
        for interval in intervals:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1] = [min(result[-1][0], interval[0]), max(result[-1][1], interval[1])]
        return result


class MergeIntervals:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    x = Solution().merge(intervals)
    print(x)
