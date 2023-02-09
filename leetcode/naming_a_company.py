from typing import List
from collections import Counter

# for explanation refer solution
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        charArr = [[] for _ in range(26)]

        def findDup(arr1, arr2) -> int:
            m1 = Counter(arr1)
            c = 0
            for i in arr2:
                if i in m1:
                    c += 1
            return c

        for i in ideas:
            charArr[ord(i[0]) - 97].append(i[1:])
        charArr = list(filter(lambda x: len(x) > 0, charArr))
        totalCount = 0
        for i in range(len(charArr)):
            for j in range(len(charArr)):
                a1, a2 = charArr[i], charArr[j]
                if i == j:
                    continue

                dup = findDup(a1, a2)
                totalCount += (len(a1) - dup) * (len(a2) - dup)
                continue

        return totalCount


if __name__ == '__main__':
    # ideas = ["coffee", "donuts", "time", "toffee"]
    # ideas = ["aye", "bye", "alpha", "apple", "bat", "beet"]
    ideas = ["if", "both", "of", "thet", "new", "names", "are", "not", "found", "in", "the", "original"]
    # print("If both of the new names are not found in the original".lower().split(" "))
    #
    print(Solution().distinctNames(ideas))
