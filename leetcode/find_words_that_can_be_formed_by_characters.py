from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def getFreqMap(s: str):
            return Counter(s[:])

        charsFreqMap = getFreqMap(chars)
        totalLength = 0
        for word in words:
            wordFreqMap = getFreqMap(word)
            canForm = True
            for key in wordFreqMap:
                if not charsFreqMap[key] or charsFreqMap[key] < wordFreqMap[key]:
                    canForm = False
                    break
            if canForm:
                totalLength += len(word)

        return totalLength


if __name__ == '__main__':
    words = ["cat", "bat", "hat", "mat"]
    chars = "attach"
    res = Solution().countCharacters(words, chars)
    print(res)
