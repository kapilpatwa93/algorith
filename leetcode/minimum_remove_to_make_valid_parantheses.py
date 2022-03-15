class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        map = {}
        string = ""
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            elif c == ")" and len(stack) > 0:
                map[stack.pop()] = 1
                map[i] = 1

        for i in range(len(s)):
            c = s[i]
            if c == ")" or c == "(":
                if i in map:
                    string += c
            else:
                string += c

        return string


if __name__ == '__main__':
    s = "leecode()()()((()))))((((("
    res = Solution().minRemoveToMakeValid(s)
    print(res)
