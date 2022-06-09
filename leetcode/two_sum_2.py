from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            s = numbers[p1] + numbers[p2]
            if s == target:
                return [p1 + 1, p2 + 1]
            if s < target:
                p1 += 1
            if s > target:
                p2 -= 1


if __name__ == '__main__':
    numbers = [-1, 0]
    target = -1
    res = Solution().twoSum(numbers, target)
    print(res)
