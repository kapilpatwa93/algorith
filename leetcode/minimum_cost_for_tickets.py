from collections import Counter
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        allDays = [0] * 365
        m = Counter(days)

        def getPrevious(day, n):
            if day - n < 0:
                return 0
            return allDays[day - n]

        for day in range(len(allDays)):
            if day + 1 in m:
                prev = getPrevious(day, 1)
                prev7 = getPrevious(day, 7)
                prev30 = getPrevious(day, 30)
                cc = min(prev + costs[0], prev7 + costs[1], prev30 + costs[2])
                allDays[day] = cc
            else:
                allDays[day] = getPrevious(day, 1)
        return allDays[-1]


if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 365]
    costs = [2, 7, 15]
    res = Solution().mincostTickets(days, costs)
    print(res)
