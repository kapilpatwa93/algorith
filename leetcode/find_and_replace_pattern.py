from collections import Counter
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            patternMap = Counter(word)
            patternMap2 = Counter(pattern)
            isSame = True
            for p, w in zip(pattern, word):
                if type(patternMap[w]) == int and type(patternMap2[p]) == int:
                    patternMap[w] = p
                    patternMap2[p] = w
                elif patternMap[w] != p and patternMap2[p] != w:
                    isSame = False
            if isSame is True:
                res.append(word)

        return res


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc", "xaa"]
    pattern = "das"
    res = Solution().findAndReplacePattern(words, pattern)
    print(res)
