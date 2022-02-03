import collections
from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreqMap(string: str):
            return collections.Counter(string)

        def getEncodedStrFromFreqMap(map) -> str:
            string = ""
            for asciiVal in range(97, 123):
                char = chr(asciiVal)
                if char in map:
                    string = string + char + str(map[char])

            return string

        def getEncodedString(string: str) -> str:
            return getEncodedStrFromFreqMap(getFreqMap(string))

        map = dict()
        for string in strs:
            encStr = getEncodedString(string)
            if encStr in map:
                map[encStr].append(string)
            else:
                arr = [string]
                map[encStr] = arr
        return list(map.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat" , "mat"]
    res = Solution().groupAnagrams(strs)
    print(res)
