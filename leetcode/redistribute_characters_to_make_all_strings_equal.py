from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freqMap = defaultdict(lambda: 0)
        val = 0
        for word in words:
            for c in word:
                freqMap[c] += 1
                val = freqMap[c]
        isEqual = True
        for key in freqMap:
            if freqMap[key]:
                if freqMap[key] % len(words) != 0 :
                    isEqual = False
                    break
        return isEqual

if __name__ == '__main__':
    words = ["abccb", "ab", "ac"]
    res = Solution().makeEqual(words)
    print(res)
