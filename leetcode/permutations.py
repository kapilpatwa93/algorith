from typing import List, Set


class Solution:
    list = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.list = []
        self.permutations(nums, set(), [])
        return self.list

    def permutations(self, nums: List[int], set: Set[int], arr: List[int]):
        if len(arr) == len(nums):
            self.list.append(arr)
            return

        for index in range(len(nums)):
            n = nums[index]
            if n not in arr:
                s = set.copy()
                s.add(nums[index])
                a = arr[:]
                a.append(n)
                self.permutations(nums, s, a)

        return


if __name__ == '__main__':
    nums = [1,2,3]
    res = Solution().permute(nums)
    print(res)
