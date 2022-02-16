from collections import defaultdict
from typing import List

codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


def getMorseForAChar(c: str) -> str:
    return codes[ord(c) - 97]


def getMorseForStr(string: str) -> str:
    morse = ""
    for c in string:
        morse += getMorseForAChar(c)
    return morse


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseMap = defaultdict(lambda: 0)
        for w in words:
            morseMap[getMorseForStr(w)] += 1
        return len(morseMap)


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg","abc"]
    res = Solution().uniqueMorseRepresentations(words)
    print(res)
