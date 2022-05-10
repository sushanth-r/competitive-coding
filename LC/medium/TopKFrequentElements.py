from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    arr = sorted(dic, key=dic.get, reverse=True)
    return arr[:k]


class TopKFrequentElements:
    nums = list(map(int, input().split()))
    k = int(input())
    print(topKFrequent(nums, k))
