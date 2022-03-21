from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccured = {}
        for i in range(len(s)):
            lastOccured[s[i]] = i
        res = []
        count = 0
        maxLastPos = 0
        for i in range(len(s)):
            maxLastPos = max(maxLastPos, lastOccured[s[i]])
            count += 1
            if maxLastPos == i:
                res.append(count)
                count = 0
        return res


if __name__ == '__main__':
    s = "abcdslkjdfdlkfdsiouzdfgdsbnmmbnzzwqwpppp"
    res = Solution().partitionLabels(s)
    print(res)
