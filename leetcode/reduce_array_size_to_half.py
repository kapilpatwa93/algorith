from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freqMap = Counter(arr)
        newArr = [(k, v) for k, v in freqMap.items()]
        newArr.sort(key=lambda x: -x[1])
        total = len(arr)
        current = 0
        i = 0
        while current < int(total / 2):
            current += newArr[i][1]
            i += 1
        return i


if __name__ == '__main__':
    arr = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    res = Solution().minSetSize(arr)
    print(res)
