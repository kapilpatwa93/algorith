import math
from heapq import heappush, heappop
from typing import List


class Solution:
    maxScore = 0

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        h = []
        zipped = list(zip(nums1, nums2))
        zipped.sort(key=lambda a: -a[1])
        for a, b in zipped:
            heappush(h, a)
            total += a
            if len(h) > k:
                total -= heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res
    
    # tle
    def maxScore1(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.maxScore = 0

        def recurse(current: int, sumNum1: int, total: int, minNum2):
            if k == total:
                print("arr minnum2", sumNum1, minNum2)
                self.maxScore = max(sumNum1 * minNum2, self.maxScore)
                return
            for i in range(current + 1, len(nums1)):
                recurse(i, sumNum1 + nums1[i], total + 1, min(minNum2, nums2[i]))

        recurse(-1, 0, 0, math.inf)
        # recurse(-1, [], math.inf)
        return self.maxScore


if __name__ == '__main__':
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    # nums1 = [4, 2, 3, 1, 1]
    # nums2 = [7, 5, 10, 9, 6]
    # k = 2
    res = Solution().maxScore(nums1, nums2, k)
    print(res)
