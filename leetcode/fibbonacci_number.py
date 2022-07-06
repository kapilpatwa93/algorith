class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a1 = 0
        a2 = 1
        c = 2
        while c <= n:
            total = a1 + a2
            a1 = a2
            a2 = total
            c += 1
        return total


if __name__ == '__main__':
    n = 10
    res = Solution().fib(n)
    print(res)
