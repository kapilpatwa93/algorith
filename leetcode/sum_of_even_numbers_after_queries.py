from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        evenTotal = 0
        res = []
        flag = [False] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                flag[i] = True
                evenTotal += nums[i]
        for q in queries:
            numToAdd, index = q[0], q[1]
            newNum = nums[index] + numToAdd

            if newNum % 2 == 0:
                evenTotal += numToAdd
                if flag[index] is False:
                    evenTotal += nums[index]
                    flag[index] = True
            else:
                if flag[index] is True:
                    evenTotal -= nums[index]
                    flag[index] = False
            nums[index] = newNum

            res.append(evenTotal)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    res = Solution().sumEvenAfterQueries(nums, queries)
    print(res)
