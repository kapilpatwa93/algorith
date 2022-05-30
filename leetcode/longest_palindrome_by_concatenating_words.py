from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = Counter(words)
        total = 0
        oddAdded = False

        def opposite(word: str) -> str:
            return f"{word[1]}{word[0]}"

        for w in m:
            opp = opposite(w)
            if opp in m and opp != w:
                count = min(m[w], m[opp])
                m[w] -= count
                m[opp] -= count
                total += count * 4
            if opp == w:
                if m[w] >= 2:
                    count = int(m[w] / 2) * 2
                    m[w] -= count
                    total += count * 2
                if oddAdded is False and m[w] > 0:
                    count = m[w]
                    m[w] = 0
                    total += count * 2
                    oddAdded = True
        return total


if __name__ == '__main__':
    words = ["ab", "ty", "yt", "lc", "cl", "ab", "bb", "cc", "cc"]
    res = Solution().longestPalindrome(words)
    print(res)
