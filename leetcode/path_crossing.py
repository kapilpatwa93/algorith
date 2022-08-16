class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = {}
        currentX, currentY = 0, 0
        points[(currentX, currentY)] = 1
        for p in path:
            if p == "N":
                currentY += 1
            if p == "S":
                currentY -= 1
            if p == "E":
                currentX += 1
            if p == "W":
                currentX -= 1
            if (currentX, currentY) in points:
                return True
            points[(currentX, currentY)] = 1
        return False


if __name__ == '__main__':
    path = "NEWS"
    res = Solution().isPathCrossing(path)
    print(res)
