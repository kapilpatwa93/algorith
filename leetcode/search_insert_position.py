from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int(((end - start) / 2) + start)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            if target < nums[mid]:
                end = mid - 1
        if target < nums[mid]:
            return mid
        else:
            return mid + 1


def main():
    nums = [1]
    target = 2
    res = Solution().searchInsert(nums, target)
    print(res)


main()
