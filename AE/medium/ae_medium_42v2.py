def staircaseTraversal(height, max_steps):
    # O(n) - Time & O(n) - Space
    cur = 0
    dp = [1]

    for i in range(1, height + 1):
        start_of_previous_window = i - max_steps - 1
        end_of_current_window = i - 1
        if start_of_previous_window >= 0:
            cur -= dp[start_of_previous_window]
        cur += dp[end_of_current_window]
        dp.append(cur)
    return dp[height]


class StairCaseTraversal:
    height = int(input())
    max_steps = int(input())
    print(staircaseTraversal(height, max_steps))
