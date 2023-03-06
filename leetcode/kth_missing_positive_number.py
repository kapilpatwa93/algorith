from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = int((start + end) / 2)
            diff = arr[mid] - (mid + 1)
            if diff >= k:
                end = mid - 1
            else:
                start = mid + 1
        return start + k


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 11]
    k = 2
    res = Solution().findKthPositive(arr, k)
    print(res)
