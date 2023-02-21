from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        def sameElement(element, index):
            if index < 0 or index > len(nums) - 1:
                return False
            return nums[index] == element

        while start < end:
            mid = int(end - start / 2) + start
            if not sameElement(nums[mid], mid + 1) and not sameElement(nums[mid], mid - 1):
                return nums[mid]
            #  get the distance between start and mid and if it is odd then do mid+1/mid-1 else keep it as mid
            isOdd = (mid - start) % 2 == 1
            if isOdd:
                if sameElement(nums[mid], mid - 1):
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if sameElement(nums[mid], mid - 1):
                    end = mid
                else:
                    start = mid
        return nums[start]


if __name__ == '__main__':
    # nums = [1,1, 2, 3, 3 ,4,4, 8,8]
    nums = [3, 7, 7, 10, 10, 11, 11]
    nums = [3, 3, 7, 7, 10]
    res = Solution().singleNonDuplicate(nums)
    print(res)
