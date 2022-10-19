from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqMap = Counter(words)
        arr = [(freqMap[x], x) for x in freqMap]
        # people.sort(key=lambda x: (-x[0], x[1]))
        arr.sort(key=lambda x: (-x[0], x[1]))

        return [arr[i][1] for i in range(k)]


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    res = Solution().topKFrequent(words, k)
    print(res)
