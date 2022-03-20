def mergeOverlappingIntervals(intervals):
    index = 0
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    intervals.sort()
    while index < len(sorted_intervals) - 1:
        current_interval = sorted_intervals[index]
        next_interval = sorted_intervals[index + 1]
        if current_interval[1] < next_interval[0]:
            index += 1
        else:
            current_interval[1] = max(current_interval[1], next_interval[1])
            sorted_intervals.pop(index + 1)

    return sorted_intervals


class MergeOverlappingIntervals:
    intervals = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]
    print(mergeOverlappingIntervals(intervals))
