import heapq
import math
from typing import List

import heapq
import math
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        que = []

        def isOdd(num):
            return num % 2 == 1

        for i in nums:
            if isOdd(i):
                i = i * 2
            heapq.heappush(que, -i)
        minDev = math.inf
        while True:

            largest = abs(heapq.nsmallest(1, que)[0])
            smallest = abs(heapq.nlargest(1, que)[0])
            num = heapq.heappop(que)
            minDev = min(minDev, largest - smallest)
            if isOdd(largest):
                break
            if not isOdd(num):
                num = int(abs(num) / 2) * -1

            heapq.heappush(que, num)
        return minDev


class Solution1:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        pq = []
        min_val = nums[0] * 2

        for num in nums:
            if num % 2 != 0:
                num *= 2
            heapq.heappush(pq, -num)
            min_val = min(num, min_val)

        ans = -pq[0] - min_val
        while pq[0] % 2 == 0:
            top = -heapq.heappop(pq)
            heapq.heappush(pq, -(top // 2))
            ans = min(ans, top - min_val)
            min_val = min(min_val, top // 2)

        return min(ans, -pq[0] - min_val)


if __name__ == '__main__':
    nums = [1, 3, 1024]
    # nums = [2,10,8]
    # nums = [3,5]
    nums = [1, 2048]
    res = Solution().minimumDeviation(nums)
    print(res)
