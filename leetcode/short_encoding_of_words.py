from collections import Counter
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        m = Counter(words)
        total = 0
        words.sort(key=lambda x: -len(x))
        print(words)
        s = ""
        for w in words:
            if m[w] != 0:
                for i in range(1, len(w)):
                    w1 = w[i:len(w)]
                    if w1 in m and m[w1] > 0:
                        m[w1] -= 1
                total += len(w) + 1
                s += w
                m[w] = 0


        print(s)
        return total


if __name__ == '__main__':
    words = ["k", "kk","kkk", "kkkk", "kapil", "pil", "mpil"]
    res = Solution().minimumLengthEncoding(words)
    print(res)
