from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        if i == len(nums1):
            arr += nums2[j:]
        else:
            arr += nums1[i:]

        arr_len = len(arr)
        if not arr:
            return 0
        if arr_len % 2:
            return arr[arr_len // 2]
        else:
            return (arr[(arr_len // 2) - 1] + arr[arr_len // 2]) / 2


class MedianOfTwoSortedArrays:
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    x = Solution().findMedianSortedArrays(nums1, nums2)
    print(x)
