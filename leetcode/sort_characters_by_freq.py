from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = Counter(s[:])
        arr = []
        for key in freqMap:
            arr.append([key, freqMap[key]])

        arr.sort(key=lambda x: -x[1])
        s = ""
        for val in arr:
            for c in range(val[1]):
                s += val[0]
        return s


if __name__ == "__main__":
    s = "tree"
    res = Solution().frequencySort(s)
    print(res)