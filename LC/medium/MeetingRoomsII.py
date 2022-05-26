from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = list()
        rooms.append(intervals[0][1])
        rooms_required = 1
        for interval in intervals[1:]:
            flag = False
            for i in range(len(rooms)):
                if interval[0] >= rooms[i]:
                    rooms[i] = interval[1]
                    flag = True
                    break
            if not flag:
                rooms.append(interval[1])
        return len(rooms)

    def minMeetingRoomsII(self, intervals: List[List[int]]) -> int:

        start = [i[0] for i in sorted(intervals, key=lambda x:x[0])]
        end = [i[1] for i in sorted(intervals, key=lambda x: x[1])]
        result = 1
        count = 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                count += 1
                i += 1
                result = max(result, count)
            else:
                count -= 1
                j += 1
        return result


class MeetingRoomsII:
    intervals = [[0,30],[5,10],[10,20]]
    x = Solution().minMeetingRoomsII(intervals)
    print(x)
