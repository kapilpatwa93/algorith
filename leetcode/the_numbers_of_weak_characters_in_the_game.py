import math
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: x[0])

        prevMaxDef = 0
        prevAttack = math.inf
        newMaxDef = 0
        totalCount = 0

        for i in range(len(properties) - 1, -1, -1):
            if properties[i][0] < prevAttack:
                prevAttack = properties[i][0]
                prevMaxDef = newMaxDef
            if properties[i][1] < prevMaxDef:
                print(properties[i])
                totalCount += 1

            newMaxDef = max(newMaxDef, properties[i][1])

        return totalCount


if __name__ == '__main__':
    properties = [[5, 2], [7, 3], [1, 6], [2, 3], [3, 9], [4, 8], [6, 7], [8, 4], [2, 3], [2, 4]]
    res = Solution().numberOfWeakCharacters(properties)
    print(res)
