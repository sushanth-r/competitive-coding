from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        overlap_count = 0
        for interval in intervals[1:]:
            if interval[0] >= prev[1]:
                prev = interval
            else:
                prev[1] = min(interval[1], prev[1])
                overlap_count += 1
        return overlap_count


class NonOverlappingIntervals:
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    x = Solution().eraseOverlapIntervals(intervals)
    print(x)
