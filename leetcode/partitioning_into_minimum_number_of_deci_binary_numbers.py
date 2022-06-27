import functools


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n[:])


if __name__ == '__main__':
    n = "908"
    print()
    res = Solution().minPartitions(n)
    print(res)
