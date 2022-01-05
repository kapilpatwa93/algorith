import math
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fb = {}

        def hasFruit(fruit):
            return fruit in fb

        def removeFruit():
            try:
                smallest = math.inf
                smallestKey = -1
                for key in fb:
                    if fb[key] < smallest:
                        smallest = fb[key]
                        smallestKey = key

                index = fb[smallestKey]
                del fb[smallestKey]
                return index
            except:
                return -1

        def addFruit(fruit, index):
            fb[fruit] = index

        def fruitCount():
            return len(fb)

        addFruit(fruits[0], 0)
        if len(fruits) > 1:
            addFruit(fruits[1], 1)
        else:
            return 1
        p1 = 0
        p2 = 1
        maxA = len(fb)
        while p2 < len(fruits) and p1 < len(fruits):
            if hasFruit(fruits[p2]):
                addFruit(fruits[p2], p2)
                p2 += 1
            elif not hasFruit(fruits[p2]) and fruitCount() == 1:
                addFruit(fruits[p2], p2)
                p2 += 1
            else:
                removedIndex = removeFruit()
                addFruit(fruits[p2], p2)
                maxA = max(p2 - p1, maxA)
                p1 = removedIndex + 1
                p2 += 1
            maxA = max(p2 - p1, maxA)
        return maxA


if __name__ == '__main__':
    fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]
    res = Solution().totalFruit(fruits)
    print(res)
