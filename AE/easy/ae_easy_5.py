import itertools
from functools import reduce


def nonConstructibleChange(coins):
    subset_sum_list = list()
    for L in range(0, len(coins) + 1):
        for subset in itertools.combinations(coins, L):
            if not subset:
                continue
            subset_sum = reduce(lambda x, y: x + y, subset)
            subset_sum_list.append(subset_sum)
    index = 1
    while index >= 0:
        if index not in subset_sum_list:
            return index
        index += 1


class NonConstructibleChange:
    coins = list(map(int, input().split()))
    print(nonConstructibleChange(coins))
