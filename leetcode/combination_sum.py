from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def findSum(arr: List[int], sum: int, currIndex: int):
            if sum == target:
                result.append(arr)
                return

            if sum > target:
                return

            for index in range(currIndex, (len(candidates))):
                num = candidates[index]
                a = arr[:]
                a.append(num)
                findSum(a, sum + num, index)

        findSum([], 0, 0)
        return result


if __name__ == '__main__':
    candidates = [5, 2, 4, 3]
    target = 8
    res = Solution().combinationSum(candidates, target)
    print(res)
