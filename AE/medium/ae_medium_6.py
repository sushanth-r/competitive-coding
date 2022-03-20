def longestPeak(array):
    array_length = len(array)
    if array_length < 3:
        return 0
    max_peak = 0
    current_peak = 1
    is_peak_reached = False
    for index in range(array_length - 1):
        if array[index] < array[index + 1]:
            if not is_peak_reached:
                current_peak += 1
            else:
                max_peak = current_peak if current_peak > max_peak and current_peak >= 3 else max_peak
                current_peak = 2
                is_peak_reached = False
        elif array[index] > array[index + 1]:
            if current_peak >= 2:
                if not is_peak_reached:
                    is_peak_reached = True
                    current_peak += 1
                    if current_peak > max_peak:
                        max_peak = current_peak
                else:
                    current_peak += 1
                    max_peak = current_peak if current_peak > max_peak and current_peak >= 3 else max_peak
            else:
                current_peak = 1
                is_peak_reached = False
        else:
            current_peak = 1
    return max_peak


class LongestPeak:
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array))
