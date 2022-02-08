class Solution:
    def addDigits(self, num: int) -> int:
        def recursiveAdd(num: int) -> int:
            if num == 0:
                return 0
            count = 0
            total = 0
            while num > 0:
                total = total + (num % 10)
                num = int(num / 10)
                count += 1
            if count != 1:
                return recursiveAdd(total)
            else:
                return total

        return recursiveAdd(num)


if __name__ == '__main__':
    num = 11
    res = Solution().addDigits(num)
    print(res)
