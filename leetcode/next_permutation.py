from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        l = len(nums)
        if l == 1:
            return
        i = 0
        for i in reversed(range(1, l)):
            if nums[i] > nums[i - 1]:
                found = True
                break
        n1 = i - 1
        n = i
        j = l - 1
        greaterDone = False

        while n <= j:
            if nums[j] > nums[n1] and greaterDone is False and found is True:
                greaterDone = True
                nums[n1], nums[j] = nums[j], nums[n1]
            j -= 1

        i = n if found else n1
        j = len(nums) - 1

        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 4, 3, 5, 3, 5, 67, 7, 4, 6, 67, 4, 67, 87, 5, 3]
    Solution().nextPermutation(nums)
    print(nums)
