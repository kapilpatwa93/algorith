import math
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p1 = -1
        p2 = -1
        index = -1
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if arr[mid] == x:
                p1 = mid
                p2 = mid + 1
                break
            elif arr[mid] < x:
                start = mid + 1

            else:
                end = mid - 1
            p1 = mid - 1
            p2 = mid
        index = 0
        minVal = math.inf
        count = 0
        mid = mid - 1
        while count < 5:
            if mid >= 0 and mid < len(arr):
                if abs(arr[mid] - x) < minVal:
                    minVal = abs(arr[mid] - x)
                    index = mid
            mid += 1
            count += 1
        p1 = index
        p2 = p1 + 1
        count = 0
        res = []

        while count < k:
            n2 = math.inf
            if p2 < len(arr):
                n2 = abs(arr[p2] - x)
            n1 = math.inf
            if p1 >= 0:
                n1 = abs(arr[p1] - x)
            if n2 < n1:
                res.append(arr[p2])
                p2 += 1
            else:
                res.append(arr[p1])
                p1 -= 1
            count += 1

        res.sort()
        return res



if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    k = 5
    x = 4
    res = Solution().findClosestElements(arr, k, x)
    print(res)
