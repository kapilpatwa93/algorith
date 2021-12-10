from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumArr = [-1 for _ in nums]
        sumArr[0] = nums[0]
        maxNo = sumArr[0]
        for index in range(1, len(nums)):
            sumArr[index] = max(sumArr[index - 1] + nums[index], nums[index])
            if sumArr[index] > maxNo:
                maxNo = sumArr[index]

        return maxNo


def main():
    nums = [5, 4, -1, 7, 8]
    res = Solution().maxSubArray(nums)
    print(res)


main()
