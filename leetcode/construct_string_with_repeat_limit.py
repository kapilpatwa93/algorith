from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        freqMap = Counter(s[:])
        freqArr = []
        for i in reversed(range(97, 123)):
            c = chr(i)

            if c in freqMap:
                freqArr.append([c, freqMap[c]])
        ss = ""
        i = 0
        while i < len(freqArr) - 1:

            while freqArr[i][1] > 0:
                c = freqArr[i][0]
                val = freqArr[i][1]
                count = max(min(k, val), 0)
                freqArr[i][1] -= count
                if ss[-1:] == c:
                    continue
                ss = ss + c * count
                if freqArr[i][1] > 0 and i + 1 < len(freqArr):
                    c = freqArr[i + 1][0]
                    val = freqArr[i + 1][1]
                    count = max(min(1, val), 0)
                    freqArr[i + 1][1] -= count
                    if ss[-1:] == c:
                        continue
                    ss = ss + c * count
                    if freqArr[i + 1][1] <= 0:
                        freqArr.pop(i + 1)

            i += 1

        if i < len(freqArr):
            c = freqArr[i][0]
            val = freqArr[i][1]
            count = max(min(k, val), 0)
            ss = ss + c * count
        return ss


if __name__ == '__main__':
    s = "bplpcfifosybmjxphbxdltxtfrjspgixoxzbpwrtkopepjxfooazjyosengdlvyfchqhqxznnhuuxhtbrojyhxwlsrklsryvmufoibgfyxgjw"
    k = 1
    res = Solution().repeatLimitedString(s, k)
    print(res)
