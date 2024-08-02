from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1 = 0
        for i in nums:
            if i == 1:
                count1 += 1

        count0 = 0
        for i in range(count1):
            if nums[i] == 0:
                count0 += 1
        ans = count0
        prev = 0
        for i in range(count1,len(nums)+count1):
            valI = i % len(nums)
            if nums[valI] == 0:
                count0 +=1
            if nums[prev] == 0:
                count0 -=1
            prev +=1
            ans = min(ans,count0)
        # for i in range(len[nums] + count1):
        
        return ans
        

if __name__ == "__main__":
    # nums = [0,1,1,1,0,0,1,1,0] # 2
    nums = [0,1,0,1,1,0,0] # 1
    nums = [0,0,0,1,1,0,1]
    res = Solution().minSwaps(nums)
    print(res)