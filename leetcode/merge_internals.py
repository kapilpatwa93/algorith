from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedArr = sorted(intervals, key=lambda x: (x[0], x[1]))
        start = sortedArr[0][0]
        end = sortedArr[0][1]
        arr = []
        for i in sortedArr:
            if end >= i[0]:
                end = max(i[1], end)
            else:
                arr.append([start, end])
                start = i[0]
                end = i[1]
        if start is not None or end is not None:
            arr.append([start, end])
        return arr

if __name__ == '__main__':
    arr = [[8,10],[15,18],[1,3],[2,6],[1,2],[1,6],[6,15],[20,21],[21,22]]
    res = Solution().merge(arr)
    print(res)