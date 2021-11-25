class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count = count + (n % 2)
            n = int(n / 2)

        return count


def main():
    n = 3
    res = Solution().hammingWeight(n)
    print(res)


main()
