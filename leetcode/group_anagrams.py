from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = {}

        def mapToString(freqMap):
            s = ""
            for i in range(97, 123):
                c = chr(i)
                if c in freqMap and freqMap[c] > 0:
                    s += c + str(freqMap[c])
            return s

        mapToString({})
        for s in strs:
            freqMap = Counter(s)
            encoded = mapToString(freqMap)
            arr = aMap[encoded] if encoded in aMap else []
            arr.append(s)
            aMap[encoded] = arr

        return aMap.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "mat"]
    res = Solution().groupAnagrams(strs)
    print(res)
