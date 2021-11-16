from typing import List


def charAt(string: str, index: int) -> str:
    return string[index] if index < len(string) else ""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 0:
            return lcp
        index = 0
        while (True):
            ch = charAt(strs[0], index)
            if ch == "":
                return lcp
            for str in strs:
                ch1 = charAt(str, index)
                if ch1 == "" or ch1 != ch:
                    return lcp
            lcp = lcp + ch
            index += 1


def main():
    strs = ["kap", "kapi", "kapil"]
    res = Solution().longestCommonPrefix(strs)
    print(res)


main()
