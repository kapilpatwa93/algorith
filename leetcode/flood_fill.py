from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        res = image
        queue = [[sr, sc]]
        color = image[sr][sc]

        def isSameColor(x, y) -> bool:
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return False
            return image[x][y] == color

        index = 0
        while index < len(queue):
            curr = queue[index]
            if isSameColor(curr[0],curr[1]):
                res[curr[0]][curr[1]] = newColor
            if isSameColor(curr[0] - 1, curr[1]):
                queue.append([curr[0] - 1, curr[1]])
            if isSameColor(curr[0] + 1, curr[1]):
                queue.append([curr[0] + 1, curr[1]])
            if isSameColor(curr[0], curr[1] + 1):
                queue.append([curr[0], curr[1] + 1])
            if isSameColor(curr[0], curr[1] - 1):
                queue.append([curr[0], curr[1] - 1])
            index += 1
        return res


def main():
    image = [[0,0,0],[0,1,0]]
    sr = 1
    sc = 1
    newColor = 2
    res = Solution().floodFill(image, sr, sc, newColor)
    print(res)


main()
