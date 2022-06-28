import heapq
import math
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        m = Counter(s)
        total = 0
        pq = []
        for c in m:
            heapq.heappush(pq, (-m[c], c))
        maxAllowed = math.inf
        for _ in m:
            a = heapq.heappop(pq)
            mCount = -a[0]
            if mCount < maxAllowed:
                maxAllowed = mCount - 1
            else:
                total += mCount - maxAllowed
                maxAllowed = max(0, maxAllowed - 1)
        return total


if __name__ == '__main__':
    s = "aaccnnddsseeddff"
    res = Solution().minDeletions(s)
    print(res)
