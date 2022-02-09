from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freqMap = Counter(nums)
        count = 0
        for key in freqMap:
            diff = key + k
            if diff in freqMap:
                if key == diff and freqMap[diff] > 1:
                    count += 1
                if key != diff:
                    count += 1
        return count


if __name__ == '__main__':
    list = [1, 2, 3, 4]
    k = 2
    res = Solution().findPairs(list, k)
    print(res)
