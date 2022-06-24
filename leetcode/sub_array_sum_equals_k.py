from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 1
        total = nums[i]
        length = len(nums)
        count = 0
        while i < length:
            if k > 0:

                if total == k:
                    count += 1
                    total -= nums[i]
                    i += 1
                elif total > k:
                    total -= nums[i]
                    i += 1
                elif j < length:
                    total += nums[j]
                    j += 1
                else:
                    i += 1
            else:
                if total == k:
                    count += 1
                    total -= nums[i]
                    i += 1
                elif total <= k:
                    total -= nums[i]
                    i += 1
                elif j < length:
                    total += nums[j]
                    j += 1
                else:
                    i += 1
        return count


if __name__ == '__main__':
    nums = [-2, -3, 3, -3, 3]
    k = 0
    res = Solution().subarraySum(nums, k)
    print(res)
