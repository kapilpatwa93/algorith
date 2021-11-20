from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        index = 0
        length = len(nums)
        if length == 0:
            return 0
        while index < length:
            if nums[pos] != nums[index]:
                pos += 1
                nums[pos] = nums[index]
            index += 1
        return pos + 1


def main():
    nums = [1, 1, 2]
    res = Solution().removeDuplicates(nums)
    print(res)


main()
