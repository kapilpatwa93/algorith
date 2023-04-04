from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        m = defaultdict(lambda: -1)
        count = 0
        start = 0

        for i in range(len(s)):
            c = s[i]
            if m[c] >= start:
                start = i
                count += 1
            m[c] = i
        return count + 1


if __name__ == '__main__':
    s = "asasasassaf"
    res = Solution().partitionString(s)
    print(res)
