import string


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        indexMap = {}
        rowCount = 0
        colCount = 0
        current = "a"
        for c in string.ascii_lowercase:
            indexMap[c] = [rowCount, colCount]
            colCount += 1
            if colCount == 5:
                rowCount += 1
                colCount = 0

        def getXMoves(current, new):
            diff = current - new
            if diff < 0:
                return "D" * abs(diff)
            elif diff > 0:
                return "U" * abs(diff)
            return ""

        def getYMoves(current, new):
            diff = current - new
            if diff < 0:
                return "R" * abs(diff)
            elif diff > 0:
                return "L" * abs(diff)
            return ""

        s = ""
        for c in target:
            currentX, currentY = indexMap[current][0], indexMap[current][1]
            newX, newY = indexMap[c][0], indexMap[c][1]
            x = getXMoves(currentX, newX)
            y = getYMoves(currentY, newY)
            newS = x + y
            if newY < currentY:
                newS = y + x
            s += newS + "!"
            current = c
        return s


if __name__ == '__main__':
    target = "leet"

    res = Solution().alphabetBoardPath(target)
    print(res)
