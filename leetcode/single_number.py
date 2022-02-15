from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for i in range(1, len(nums)):
            n = n ^ nums[i]
        return n

if __name__ == '__main__':
    nums = [1,2,2]
    res = Solution().singleNumber(nums)
    print(res)

