from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i

        def isValid(word1: str, word2: str) -> bool:
            minLength = min(len(word1), len(word2))
            for i in range(minLength):
                if orderMap[word1[i]] < orderMap[word2[i]]:
                    return True
                if orderMap[word1[i]] > orderMap[word2[i]]:
                    return False
            if len(word1) > len(word2):
                return False
            return True

        for i in range(1, len(words)):

            if not isValid(words[i - 1], words[i]):
                return False

        return True


if __name__ == '__main__':
    words = ["apap", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    res = Solution().isAlienSorted(words, order)
    print(res)
