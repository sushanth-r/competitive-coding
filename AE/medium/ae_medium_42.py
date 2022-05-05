def staircaseTraversal(height, max_steps):
    # Time - O(n*k), Space - O(n)
    dp = [0 for _ in range(height + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, height + 1):
        j = i - 1
        curr_steps = 1
        while curr_steps <= max_steps:
            dp[i] += dp[j]
            curr_steps += 1
            j -= 1
    return dp[height]


class StairCaseTraversal:
    height = int(input())
    max_steps = int(input())
    print(staircaseTraversal(height, max_steps))
