from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [[i, sum(mat[i])] for i in range(len(mat))]
        arr.sort(key=lambda x: x[1])
        final = [arr[i][0] for i in range(k)]
        return final


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    k = 3
    res = Solution().kWeakestRows(mat, k)
    print(res)
