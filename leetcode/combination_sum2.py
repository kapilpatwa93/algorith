from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        print(candidates)

        def findSum(arr: List[int], sum: int, currIndex: int):
            if sum == target:
                result.append(arr)
                return

            if sum > target:
                return

            prev = None
            for index in range(currIndex, (len(candidates))):
                num = candidates[index]
                if not (num == prev):
                    a = arr[:]
                    a.append(num)
                    findSum(a, sum + num, index + 1)
                prev = num

        findSum([], 0, 0)
        return result


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = Solution().combinationSum2(candidates, target)
    print(res)
