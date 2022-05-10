from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def recurse(arr: List[int], currentSum, lastNum):
            if len(arr) >= k:
                if currentSum == n:
                    return arr
                else:
                    return None
            if currentSum > n:
                return None

            for i in range(lastNum + 1, 10):
                a1 = arr.copy()
                a1.append(i)
                newSum = currentSum + i
                res = recurse(a1, newSum, i)
                if res is not None:
                    result.append(res)

        recurse([], 0, 0)
        return result


if __name__ == '__main__':
    k, n = 9, 45
    res = Solution().combinationSum3(k, n)
    print(res)
