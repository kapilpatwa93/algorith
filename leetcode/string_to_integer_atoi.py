class Solution:
    def myAtoi(self, s: str) -> int:
        numStarted = False
        sign = None
        num = 0
        def isSpace(ascVal):
            return ascVal == 32

        def isSign(ascVal):
            return ascVal == 45 or ascVal == 43

        def isNum(ascVal):
            return 48 <= ascVal <= 57

        for c in s:
            ascVal = ord(c)
            if not numStarted and isSpace(ascVal) and sign is None:
                continue
            elif not numStarted and isSign(ascVal) and sign is None:
                sign = ascVal
            elif isNum(ascVal):
                numStarted = True
                num = int(num * 10 + int(c))
            else:
                break

        if sign == 45:
            num *= -1
        minBound = (pow(2, 31) * -1)
        maxBound = pow(2, 31) - 1
        if num < minBound:
            return minBound
        elif num > maxBound:
            return maxBound
        return num


if __name__ == '__main__':
    s = "  +  413"
    res = Solution().myAtoi(s)
    print(res)
