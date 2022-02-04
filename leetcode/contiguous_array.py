from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        m = {}
        maxLen = 0
        for i in range(len(nums)):
            v = nums[i]
            if v == 0:
                count = count - 1
            else:
                count = count + 1

            if count in m:
                maxLen = max(maxLen,i-m[count])
            else:
                m[count] = i
        return maxLen

if __name__ == '__main__':
    nums = [0,0,1,0,0,0,1,1]
    res = Solution().findMaxLength(nums)
    print(res)