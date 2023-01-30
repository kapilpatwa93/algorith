class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0, 1, 1]
        t0, t1, t2 = 0, 1, 1
        if n <= 0:
            return 0
        if n <= 2:
            return 1
        count = 2
        while count < n:
            num = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = num
            count += 1
        # print(tribo, num)
        return num


if __name__ == '__main__':
    n = 10
    res = Solution().tribonacci(n)
    print(res)
