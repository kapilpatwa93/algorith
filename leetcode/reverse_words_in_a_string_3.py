class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""

        def reverseWord(word):
            reversed = ""
            for c in word:
                reversed = c + reversed
            return reversed

        for word in words:
            res = res + reverseWord(word) + " "

        return res.rstrip()


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    res = Solution().reverseWords(s)
    print(res)
