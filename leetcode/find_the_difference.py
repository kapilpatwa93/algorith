from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        strMap = Counter(s)
        for c in t:
            if c in strMap:
                strMap[c] = strMap[c] - 1
                if strMap[c] == 0:
                    del strMap[c]
            else:
                return c
if __name__ == '__main__':
    s = "kapil"
    t = "kapilp"
    res = Solution().findTheDifference(s,t)
    print(res)