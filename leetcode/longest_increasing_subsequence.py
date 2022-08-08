from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        m = 1
        for i in reversed(range(0, len(nums))):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], (memo[j]) + 1)
                    m = max(memo[i], m)

        return m


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 4, 3, 4, 3, 2, 12]
    res = Solution().lengthOfLIS(nums)
    print(res)
