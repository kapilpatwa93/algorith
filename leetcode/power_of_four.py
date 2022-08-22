class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = n
        if num < 1:
            return False
        while num > 0:
            if num == 1:
                return True
            rem = num % 4

            if rem != 0:
                return False
            num = num / 4
        return True


if __name__ == '__main__':
    n = 16
    res = Solution().isPowerOfFour(n)
    print(res)
