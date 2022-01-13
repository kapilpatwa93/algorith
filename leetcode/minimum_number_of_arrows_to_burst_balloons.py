from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[1],x[0]))
        arr = 0
        i = 0
        while i < len(points):
            start = points[i][1]
            i += 1
            while i < len(points) and start >= points[i][0]:
                i = i + 1
            arr += 1
        return arr


if __name__ == '__main__':
    points = [[1,2],[3,4],[5,6],[7,8]]
    res = Solution().findMinArrowShots(points)
    print(res)
