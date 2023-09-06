from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0:
            return []
        start = nums[0]
        curr = nums[0]

        def getRange(start, end):
            return str(start) if start == end else str(start) + "->" + str(end)

        for i in nums:
            prev = curr
            curr = i
            if (curr - 1) == prev:
                continue
            ranges.append(getRange(start, prev))
            start = curr

        ranges.append(getRange(start, curr))
        return ranges[1:]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 6, 7, 8, 10]
    res = Solution().summaryRanges(nums)
    print(res)
