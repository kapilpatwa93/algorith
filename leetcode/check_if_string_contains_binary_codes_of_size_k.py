import math


class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        m = dict()
        for i in range(0, len(s) - k + 1):
            m[s[i:i + k]] = 1
        has = True
        for i in range(int(math.pow(2, k))):
            key = format(i, "b").rjust(k, "0")
            if not key in m:
                has = False
        return has


if __name__ == '__main__':
    s = "1110110010000"
    k = 3
    res = Solution().hasAllCodes(s, k)
    print(res)
