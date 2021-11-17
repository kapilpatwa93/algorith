openingClosingPair = {
    "{": "}", "[": "]", "(": ")"
}


class Solution:
    def isValid(self, s: str) -> bool:
        isValid = True
        stack = list()
        for paran in s:
            if isOpening(paran):
                stack.append(paran)
            else:
                if len(stack) > 0 and paran == getClosing(stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
        return isValid and len(stack) == 0


def getClosing(parantheses: str) -> bool:
    return openingClosingPair[parantheses]


def isOpening(parantheses: str) -> bool:
    if parantheses in openingClosingPair:
        return True
    else:
        return False


def main():
    strs = "[][]"
    res = Solution().isValid(strs)
    print(res)


main()
