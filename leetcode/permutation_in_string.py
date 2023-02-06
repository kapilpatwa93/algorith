from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(lambda: 0)
        s2Map = defaultdict(lambda: 0)
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s2Map[s2[i]] += 1
            s1Map[s1[i]] += 1

        if s1Map == s2Map:
            return True
        for i in range(len(s1), len(s2)):
            removedChar = s2[i - len(s1)]
            s2Map[removedChar] -= 1
            if s2Map[removedChar] == 0:
                del s2Map[removedChar]
            s2Map[s2[i]] += 1
            if s2Map == s1Map:
                return True

        return False


if __name__ == '__main__':
    s1 = "rvwrk"
    s2 = "lznomzggwrvrkxecjaq"
    res = Solution().checkInclusion(s1, s2)
    print(res)
