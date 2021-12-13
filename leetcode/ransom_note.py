class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = getFrequencyMap(ransomNote)
        magMap = getFrequencyMap(magazine)
        canMake = True
        for key in ransomMap:
            if not (key in magMap and ransomMap[key] <= magMap[key]):
                canMake = False
                break
        return canMake


def getFrequencyMap(string: str) -> dict:
    freqMap = {}
    for index in range(len(string)):
        if not string[index] in freqMap:
            freqMap[string[index]] = 1
        else:
            freqMap[string[index]] += 1
    return freqMap


def main():
    ransomNote = "aaa"
    magazine = "ab"
    res = Solution().canConstruct(ransomNote, magazine)
    print(res)


main()
