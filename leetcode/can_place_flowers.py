from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def canPlace(i):
            if flowerbed[i] == 1:
                return False
            if i >= 1 and flowerbed[i - 1] == 1:
                return False
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                return False
            return True

        for i in range(0, len(flowerbed)):
            if canPlace(i):
                flowerbed[i] = 1
                n = n - 1
                if n <= 0:
                    return True
        return n == 0


if __name__ == '__main__':
    flowerbed = [0, 0, 0, 0, 0, 1, 0, 0]
    n = 1
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)