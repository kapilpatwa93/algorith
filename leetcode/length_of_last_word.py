class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        isWord = False
        index = len(s) - 1
        length = 0
        while index >= 0:
            if not isWord and s[index] != " ":
                isWord = True
            if isWord:
                if s[index] != " ":
                    length += 1
                else:
                    return length
            index -= 1
        return length