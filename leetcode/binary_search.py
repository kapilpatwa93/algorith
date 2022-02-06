from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        index = -1
        while start <= end:
            mid = int((start + end) / 2)
            print(mid, start, end)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return index


def main():
    nums = [-1, 0, 3, 5, 9, 12, 14]

    target = 9
    res = Solution().search(nums, target)
    print(res)


main()
