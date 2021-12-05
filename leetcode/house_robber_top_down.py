from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robTopDown(nums)

    def robTopDown(self, nums: List[int]) -> int:
        table = [None for _ in nums]

        def getVal(index: int) -> int:
            return 0 if index < 0 else table[index]

        for index in range(len(nums)):
            table[index] = max(getVal(index - 2) + nums[index], getVal(index - 3) + nums[index])
        return max(table[len(nums) - 1], table[len(nums) - 2])

    memo = []


def main():
    nums = [2, 1, 1, 2, 3]
    res = Solution().rob(nums)
    print(res)


main()
