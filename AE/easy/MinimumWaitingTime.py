def minimumWaitingTime(queries: list):
    queries.sort()
    total_wait_time = 0
    wait_time = 0
    index = 1
    while index < len(queries):
        wait_time += queries[index-1]
        total_wait_time += wait_time
        index += 1
    return total_wait_time


class MinimumWaitingTime:
    input_list = list(map(int, input().split()))
    print(minimumWaitingTime(input_list))
