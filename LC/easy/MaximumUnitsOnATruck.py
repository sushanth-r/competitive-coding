from typing import List


class Solution:
    def maximumUnits(self, box_types: List[List[int]], truck_size: int) -> int:
        box_types = sorted(box_types, key=lambda x: x[1], reverse=True)
        current_size, maximum_units = 0, 0
        i = 0
        while current_size < truck_size and i < len(box_types):
            if current_size + box_types[i][0] <= truck_size:
                current_size += box_types[i][0]
                maximum_units += (box_types[i][0] * box_types[i][1])
            else:
                remaining_size = truck_size - current_size
                current_size += remaining_size
                maximum_units += (remaining_size * box_types[i][1])
            i += 1
        return maximum_units


class MaximumUnitsOnATruck:
    box_types = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
    truck_size = int(input())
    x = Solution().maximumUnits(box_types, truck_size)
    print(x)
