from collections import Counter
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        total = 0
        for n in freqMap:
            if n-1 not in freqMap:
                p = n
                counter = 0
                while p in freqMap:
                    p +=1
                    counter +=1
                total = max(total,counter)
        return total

if __name__ == '__main__':
    list = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    res = Solution().longestConsecutive(list)
    print(res)
