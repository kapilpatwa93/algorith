from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prevChar = ""
        res = ""
        i = 0
        pointer = 0
        while i < len(chars):
            c = chars[i]
            count = 0
            while i < len(chars) and chars[i] == c:
                count += 1
                i += 1
            chars[pointer] = c
            pointer += 1
            if count > 1:
                while count > 0:
                    rem = str(count % 10)
                    count = int(count / 10)
                    print(pointer)
                    chars[pointer] = rem
                    pointer += 1

        print(res, chars)
        return pointer


if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    res = Solution().compress(chars)
    print(res)
