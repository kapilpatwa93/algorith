from typing import List


class Solution:

    def totalSteps(self, nums: List[int]) -> int:
        sol = [0] * (len(nums))
        stack = []
        for i in reversed(range(0, len(nums))):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                sol[i] = max(sol[i] + 1, sol[stack[-1]])
                stack.pop()
            stack.append(i)
        return max(sol)


if __name__ == '__main__':
    nums = [6, 4, 5, 3, 7, 3, 8, 9, 5, 76, 5, 3, 45, 7, 43, 6, 45, 7, 6, 6]
    res = Solution().totalSteps(nums)
    print(res)
