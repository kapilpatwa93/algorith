class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        closed = False
        for b in s:
            if b == "(":
                stack.append(0)
                closed = False
            else:
                if closed == False:
                    stack.pop()
                    stack.append(1)
                else:
                    total = 0
                    while len(stack) > 0 and stack[-1] != 0:
                        top = stack.pop()
                        total += top

                    stack.pop()
                    stack.append(total * 2)
                closed = True
        return sum(stack)


if __name__ == '__main__':
    s = "()()"
    res = Solution().scoreOfParentheses(s)
    print(res)
