from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.permutation(nums, 0)
        return self.perms

    perms = []

    def permutation(self, nums: List[int], curr: int):
        if curr >= len(nums):
            self.perms.append(nums)
            return

        for index in range(curr, len(nums)):
            n = nums[:]
            swap(n, curr, index)
            self.permutation(n, curr + 1)
        return


def swap(arr: List[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    nums = [1, 2]
    res = Solution().permute(nums)
    print(res)
