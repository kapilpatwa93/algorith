class Solution:
    m = {}

    def isHappy(self, n: int) -> bool:
        self.m = {}

        def recursiveHappy(num: int) -> int:
            count = 0
            sum = 0

            while num > 0:
                n = num % 10
                sum += n * n
                num = int(num / 10)
                count += 1
            # print(num,sum)
            if sum in self.m:
                return False
            self.m[sum] = 1
            if sum == 1:
                return True

            return recursiveHappy(sum)

        return recursiveHappy(n)


if __name__ == '__main__':
    n = 2
    res = Solution().isHappy(n)
    print(res)
