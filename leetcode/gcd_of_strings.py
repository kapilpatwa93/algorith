class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def canDivide(word: str, divisor: str) -> bool:
            if len(word) % len(divisor) != 0:
                return False
            return (divisor * int(len(word) / len(divisor))) == word

        test = str1 if len(str1) < len(str2) else str2
        word = ""

        for i in range(len(test)):
            divisor = test[0:i + 1]
            if not (canDivide(str1, divisor) and canDivide(str2, divisor)):
                continue
            word = divisor
        return word


if __name__ == '__main__':
    str1 = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM"
    str2 = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM"
    res = Solution().gcdOfStrings(str1, str2)
    print(res)
