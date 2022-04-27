from collections import Counter
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        freqMap = Counter(arr)
        total = 0
        arr.sort()

        def getTotalTree(index: int) -> int:
            num = arr[index]
            for i in range(0, index):
                if num % arr[i] == 0:
                    freqMap[num] += freqMap[int(num / arr[i])] * freqMap[arr[i]]
            return freqMap[num]

        for i in range(len(arr)):
            total += getTotalTree(i)

        return total % (pow(10, 9) + 7)


if __name__ == '__main__':
    arr = [2, 4, 5, 7, 9, 10, 14, 16, 8]
    res = Solution().numFactoredBinaryTrees(arr)
    print(res)
