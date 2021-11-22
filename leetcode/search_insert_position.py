from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                index = mid
                break
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if index == -1:
            if nums[mid] > target:
                index = mid
            else:
                index = mid + 1
        return index


def main():
    nums = [1]
    target = 2
    res = Solution().searchInsert(nums, target)
    print(res)


main()
