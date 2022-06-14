class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2))] for _ in range(len(word1))]

        def lcs(word1: str, word2: str, start1: int, start2: int) -> int:
            if start1 >= len(word1) or start2 >= len(word2):
                return 0
            if memo[start1][start2] is not None:
                return memo[start1][start2]

            if word1[start1] == word2[start2]:
                return lcs(word1, word2, start1 + 1, start2 + 1) + 1
            memo[start1][start2] = max(lcs(word1, word2, start1 + 1, start2), lcs(word1, word2, start1, start2 + 1))
            return memo[start1][start2]

        maxCount = lcs(word1, word2, 0, 0)
        return len(word2) + len(word1) - (maxCount * 2)


if __name__ == '__main__':
    word2 = "plasma"
    word1 = "altruism"
    res = Solution().minDistance(word1, word2)
    print(res)
