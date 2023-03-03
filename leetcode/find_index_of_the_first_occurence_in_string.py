class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        nLen = len(needle)
        hLen = len(haystack)
        if nLen > hLen:
            return -1
        while i < len(haystack):
            if (i + nLen) > hLen:
                return -1
            # print(haystack[i:i+nLen])
            if haystack[i:i + nLen] == needle:
                return i
            i += 1
        return -1


if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leet"
    print(Solution().strStr(haystack, needle))
