from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        freqArr = Counter(changed)
        res = []
        for i in changed:
            if freqArr[i] != 0:
                if freqArr[i * 2] != 0:
                    freqArr[i] -= 1
                    freqArr[i * 2] -= 1
                    res.append(i)
                else:
                    return []
        for i in freqArr:
            if freqArr[i] != 0:
                return []
        return res


if __name__ == '__main__':
    changed = [1, 2, 2, 4]
    res = Solution().findOriginalArray(changed)
    print(res)
