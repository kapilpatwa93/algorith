from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def isPredecessor(w1: str, w2: str) -> bool:
            misCount = 0
            if len(w1) + 1 != len(w2):
                return False
            i = 0
            j = 0
            while i < len(w1) and j < len(w2):
                if w1[i] == w2[j]:
                    i += 1
                else:
                    misCount += 1
                j += 1
            return misCount <= 1

        mem = {}

        def recurse(words: List[str], currWord: int, count: int):
            if currWord >= len(words):
                return count
            maxCount = 0
            cw = words[currWord]
            if cw in mem:
                return mem[cw]
            for i in range(currWord + 1, len(words)):
                if isPredecessor(cw, words[i]):
                    maxCount = max(maxCount, recurse(words, i, count + 1))
            mem[cw] = max(maxCount, count)
            return mem[cw]

        maxCount = 0
        for i in range(len(words)):
            maxCount = max(maxCount, recurse(words, i, 0) + 1)
        return maxCount


if __name__ == '__main__':
    words = ["ba", "bca", "bda", "bdca", "b", "a", "ab", "abc", "abcd", "abcde"]
    res = Solution().longestStrChain(words)
    print(res)
