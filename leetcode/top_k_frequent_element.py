from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        bucketArr = [[] for _ in range(len(nums))]
        for i in c:
            bucketArr[c[i] - 1].append(i)
        res = []
        total = 0
        for n in range(len(bucketArr)):
            i = bucketArr[len(bucketArr) - 1 - n]
            for j in i:
                if total == k:
                    return res
                total += 1
                res.append(j)
        return res


if __name__ == '__main__':
    k = 3
    nums = [1,1,1,2,2,3,4,4,2,2,1]
    res = Solution().topKFrequent(nums,k)
    print(res)