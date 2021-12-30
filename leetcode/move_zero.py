from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def getNextIndex(curr: int, zero: bool) -> int:
            if curr >= len(nums):
                return len(nums)
            for index in range(curr + 1, len(nums)):
                if zero:
                    if nums[index] == 0:
                        return index
                else:
                    if nums[index] != 0:
                        return index
            return len(nums)

        zPointer = getNextIndex(-1, True)
        nzPointer = getNextIndex(zPointer, False)
        pz = zPointer
        pn = nzPointer
        while zPointer < len(nums) and nzPointer < len(nums):
            print(pz, pn)
            nums[zPointer], nums[nzPointer] = nums[nzPointer], nums[zPointer]
            zPointer = getNextIndex(pz, True)
            nzPointer = getNextIndex(pn, False)
            pz = zPointer
            pn = nzPointer



if __name__ == '__main__':
    nums = [0,0,0,0,1, 2, 3, 0, 0, 0, 1, 1]
    Solution().moveZeroes(nums)
    print(nums)
