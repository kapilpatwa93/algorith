class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        indexMap = {}
        for i in range(len(s)):
            c = s[i]

            if c in indexMap:

                l = i - start
                if indexMap[c] >= start:
                    start = indexMap[c] + 1

                indexMap[c] = i

                length = max(l, length)

            indexMap[c] = i
        l = i - start + 1
        length = max(l, length)
        return length


if __name__ == '__main__':
    s = "abcaaacbad"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
