def contains_duplicate(nums: list) -> bool:
    return len(nums) != len(set(nums))


class ContainsDuplicate:
    nums = list(map(int, input().split()))
    print(contains_duplicate(nums))
