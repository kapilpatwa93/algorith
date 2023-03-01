from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 <= p2:
            maxA = max(maxA, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return maxA


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = Solution().maxArea(height)
    print(res)
