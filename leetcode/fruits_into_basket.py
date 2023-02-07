import math
from typing import List


class Solution:
    # one by one keep adding fruits in the basket, and check if the basket has more than 2 fruits,
    # if yes, then find the fruit that has to be removed and find the total count of fruits
    # which are present in the basket (count = i - fruitMap[removed])

    def totalFruit2(self, fruits: List[int]) -> int:
        fruitMap = {}
        if len(fruits) <= 2:
            return len(fruits)
        curr = fruits[0]
        fruitMap[fruits[0]] = 0
        fruitMap[fruits[1]] = 1
        maxCount = 0
        count = 0
        fruitSet = set()

        def getRemoved(curr, prev, fruitBasket):
            removed = 0
            for i in fruitBasket:
                if i != curr and i != prev:
                    removed = i
            return removed

        for i in range(len(fruits)):
            prev = curr
            curr = fruits[i]
            fruitMap[curr] = i
            fruitSet.add(curr)
            if len(fruitSet) > 2:
                removed = getRemoved(curr, prev, fruitSet)
                fruitSet.remove(removed)
                maxCount = max(maxCount, count)
                count = i - fruitMap[removed]
            else:
                count += 1
        maxCount = max(maxCount, count)
        return maxCount


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
    fruits = [1, 0, 3, 1, 4, 7, 1, 2]
    res = Solution().totalFruit(fruits)
    print(res)
