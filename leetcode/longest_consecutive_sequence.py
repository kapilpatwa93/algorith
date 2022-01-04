import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqMap = set(nums)
        longestSeq = 0
        for num in nums:
            if num - 1 not in freqMap:
                seq = 0
                seq += 1
                while num + 1 in freqMap:
                    num += 1
                    seq += 1
                longestSeq = max(seq, longestSeq)

        return longestSeq


if __name__ == '__main__':
    list = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    res = Solution().longestConsecutive(list)
    print(res)
