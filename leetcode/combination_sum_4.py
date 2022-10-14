from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = {}

        def recurse(target: int):
            if target < target:
                return 0
            if target == 0:
                return 1
            if target in m:
                return m[target]
            sum = 0
            for n in nums:

                if target >= n:
                    sum += recurse(target - n)

            m[target] = sum
            return sum

        return recurse(target)


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    target = 4
    res = Solution().combinationSum4(nums, target)
    print(res)

