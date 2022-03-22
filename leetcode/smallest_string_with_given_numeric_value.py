class Solution:

    def getSmallestString(self, n: int, k: int) -> str:
        s = ""

        def getValue(n: int, k: int) -> int:
            if k - (n - 1) >= 26:
                return 26
            else:
                return k - (n - 1)

        for i in range(n):
            val = getValue(n - i, k)
            k = k - val
            s = chr(96 + val) + s
        return s


if __name__ == '__main__':
    k = 24
    n = 3
    res = Solution().getSmallestString(n, k)
    print(res)
