import math
from typing import List


class Solution:
    # with dynamic programming
    def jump2(self, nums: List[int]) -> int:
        arr = [math.inf] * len(nums)
        arr[len(nums) - 1] = 0
        for i in reversed(range(len(nums) - 1)):
            num = nums[i]
            for j in range(1, num + 1):
                if i + j > len(nums) - 1:
                    break
                arr[i] = min(arr[i + j] + 1, arr[i])
            # print(i)
        print(arr)
        return int(arr[0])

    # with greedy
    def jump(self, nums: List[int]) -> int:
        count = 0
        p1 = 0
        p2 = 0
        for i in range(len(nums)):
            newP1 = p2 + 1
            newP2 = p2 + 1
            if p2 + 1 >= len(nums):
                return count
            for j in range(p1, p2 + 1):
                newP2 = max(newP2, nums[j] + j)

            p1 = newP1
            p2 = newP2
            count += 1

        return count


if __name__ == '__main__':
    nums = [1, 4, 1, 5, 3, 1, 2, 1, 2]
    res2 = Solution().jump2(nums)
    res = Solution().jump(nums)
    print(res, res2)
