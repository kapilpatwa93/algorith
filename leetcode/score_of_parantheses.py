class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(0)
            if s[i] == ")":

                tsum = 0
                while stack[len(stack) - 1] != 0:
                    tsum += stack[len(stack) - 1]
                    stack.pop()
                stack.pop()
                stack.append(1 if tsum == 0 else 2 * tsum)
            i += 1
        return sum(stack)


if __name__ == '__main__':
    s = "((()()))(()(()))"
    res = Solution().scoreOfParentheses(s)
    print(res)
