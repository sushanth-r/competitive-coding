from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                return False
            end = intervals[i][1]
        return True


class MeetingRooms:
    intervals = [[0,30],[40,50],[30, 35]]
    x = Solution().canAttendMeetings(intervals)
    print(x)
