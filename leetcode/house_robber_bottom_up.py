from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robBottomUp(nums)

    memo = []

    def recurse(self, nums: List[int], index: int) -> int:
        if index < 0:
            return 0
        if index == 0 or index == 1:
            self.memo[index] = nums[index]
            return nums[index]

        if self.memo[index] != -1:
            return self.memo[index]
        self.memo[index] = max(self.recurse(nums, index - 2) + nums[index],
                               self.recurse(nums, index - 3) + nums[index])
        return self.memo[index]

    def robBottomUp(self, nums: List[int]) -> int:
        self.memo = [-1 for _ in nums]
        return max(self.recurse(nums, len(nums) - 1), self.recurse(nums, len(nums) - 2))


def main():
    nums = [2, 1, 1, 2, 3]
    res = Solution().rob(nums)
    print(res)


main()
