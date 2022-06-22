import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            heapq.heappush(q, n)
        n = 0
        for i in range(len(nums) - k + 1):
            n = heapq.heappop(q)
        return n


if __name__ == '__main__':
    nums = [4, 2, 5, 6, 7, 8, 3]
    nums.sort()
    print(nums)
    k = 3
    res = Solution().findKthLargest(nums, k)
    print(res)
