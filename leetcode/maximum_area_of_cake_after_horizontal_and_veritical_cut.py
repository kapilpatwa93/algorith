from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        verticalCuts.append(0)
        horizontalCuts.sort()
        verticalCuts.sort()

        maxH = 0
        maxW = 0
        for i in range(len(horizontalCuts) - 1):
            maxH = max(maxH, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            maxW = max(maxW, verticalCuts[i + 1] - verticalCuts[i])
        return (maxW * maxH) % (pow(10, 9) + 7)


if __name__ == '__main__':
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]

    res = Solution().maxArea(h, w, horizontalCuts, verticalCuts)
    print(res)
