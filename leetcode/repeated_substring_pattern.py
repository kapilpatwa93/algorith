class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        twoS = s + s
        validTwoS = twoS[1:(
                len(twoS) - 1)]  # remove 1st and last char from concatenated str and check if og string is present
        try:
            validTwoS.index(s)
            return True
        except:
            return False


if __name__ == '__main__':
    s = "aba"
    res = Solution().repeatedSubstringPattern(s)
    print(res)
