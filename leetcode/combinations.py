from typing import List


class Solution:
    list = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.list = []
        self.combinations(n, 0, k, [])
        return self.list

    def combinations(self, n, curr, k, arr: List[int]):
        if len(arr) == k:
            self.list.append(arr[:])
            return
        index = curr
        while index < n:
            a = arr[:]
            a.append(index + 1)
            self.combinations(n, index + 1, k, a)
            index += 1
        return


if __name__ == '__main__':
    n = 4
    k = 3
    res = Solution().combine(n, k)
    print(res)
