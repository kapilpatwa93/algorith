from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        maxSum = 0
        total = 0
        maxes = [0, 0, 0]
        for j in range(min(3, k)):
            for i in range(len(arr)):
                if (total + arr[i]) < arr[i]:
                    total = arr[i]
                else:
                    total = total + arr[i]
                maxSum = max(total, maxSum)
            maxes[j] = maxSum
        if k == 1:
            return maxes[0]

        if maxes[1] == maxSum:
            return maxSum % (pow(10, 9) + 7)
        else:
            return (maxes[0] + ((maxes[1] - maxes[0]) * (k - 1))) % (pow(10, 9) + 7)


if __name__ == '__main__':
    arr = [10, 30, -50, 30, 10, 20, -20, 100, 10]
    k = 3
    res = Solution().kConcatenationMaxSum(arr, k)
    print(res)
