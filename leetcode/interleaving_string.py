class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = {}

        def recurse(i1: int, i2: int, newStr: str) -> bool:
            if newStr == s3:
                return True
            if newStr in m:

                return m[newStr]
            if i1 >= len(s1) and i2 >= len(s2):
                return False
            if i1 < len(s1):
                newStr1 = newStr + s1[i1]
                res1 = recurse(i1 + 1, i2, newStr1)
                m[newStr1] = res1
                if res1:
                    return True
            if i2 < len(s2):
                newStr2 = newStr + s2[i2]
                res2 = recurse(i1, i2 + 1, newStr2)
                m[newStr2] = res2
                return res2
            return False

        return recurse(0, 0, "")


if __name__ == '__main__':
    s1 = "abcd"
    s2 = "efgh"
    s3 = "efghabcd"
    res = Solution().isInterleave(s1, s2, s3)
    print(res)
