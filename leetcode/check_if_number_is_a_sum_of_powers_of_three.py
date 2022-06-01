import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            rem = n % 3
            if rem > 1:
                return False
            n = int(n / 3)
        return True


if __name__ == '__main__':
    n = 33
    res = Solution().checkPowersOfThree(n)
    print(res)
