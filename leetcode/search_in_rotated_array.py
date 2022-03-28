from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + int((end - start) / 2)
            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            elif nums[start] < nums[end]:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target > nums[start] > nums[mid]:
                    end = mid - 1
                elif target < nums[mid] < nums[start]:
                    end = mid - 1
                elif nums[mid] > nums[start] > target and target < nums[mid]:
                    start = mid + 1
                elif nums[start] < target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


if __name__ == '__main__':
    nums = [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 3
    res = Solution().search(nums, 11)
    print(res)
    for i in range(15):
        res = Solution().search(nums, i)
        print(i, res)
