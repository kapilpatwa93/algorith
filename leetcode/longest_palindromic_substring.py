class Solution:

    def longestPalindrome(self, s: str) -> str:

        def expand(s1:int, s2:int):
            ss = ""
            while s1 >= 0 and s2 < len(s):
                if s[s1] != s[s2]:
                    return ss
                if s1 == s2:
                    ss = s[s1]
                else:
                    ss = s[s1] + ss + s[s2]
                s1 -= 1
                s2 += 1
            return ss

        res = ""
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            s1 = expand(i, i)
            if len(s1) > len(res):
                res = s1
            s1 = expand(i, i + 1)
            if len(s1) > len(res):
                res = s1

        return res


if __name__ == '__main__':
    s = "aa"
    res = Solution().longestPalindrome(s)
    print(res)
