class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap[c] if c in freqMap else 0 + 1
        for index in range(len(s)):
            if freqMap[s[index]] == 1:
                return index
        return -1


if __name__ == '__main__':
    s = "aabb"
    res = Solution().firstUniqChar(s)
    print(res)
