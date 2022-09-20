from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        arr = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                n1, n2 = nums1[i], nums2[j]

                if n1 == n2:
                    arr[i + 1][j + 1] = arr[i][j] + 1

        return max(max(row) for row in arr)


if __name__ == '__main__':
    nums1 = [1, 3, 2, 1, 4, 1, 1]
    nums2 = [1, 3, 2, 1, 4]
    res = Solution().findLength(nums1, nums2)
    print(res)
