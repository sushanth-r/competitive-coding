class Solution:
    # Time - O(n), Space - O(n)
    def longestConsecutive(self, nums) -> int:
        nums_set = set(nums)
        longest_consecutive_sequence = 0
        for num in nums_set:
            current_consecutive_sequence = 1
            if num - 1 in nums_set:
                continue
            while num + 1 in nums_set:
                num += 1
                current_consecutive_sequence += 1
            longest_consecutive_sequence = max(longest_consecutive_sequence, current_consecutive_sequence)
        return longest_consecutive_sequence


class LongestConsecutiveSequence:
    nums = list(map(int, input().split()))
    # nums = [0,3,7,2,5,8,4,6,0,1]
    x = Solution().longestConsecutive(nums)
    print(x)
