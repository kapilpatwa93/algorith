from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        current = 0
        res = 0
        for num in nums:
            current += num
            if current - goal in count:
                res += count[current-goal]
            count[current] = count.get(current, 0) + 1
        return res


if __name__ == '__main__':
    nums = [1,0,0,0,1, 1]
    goal = 2
    res = Solution().numSubarraysWithSum(nums,goal)
    print(res)
