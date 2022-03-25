from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        final = 0
        for i in range(int(len(costs) / 2)):
            final += costs[i][0] + costs[len(costs) - 1 - i][1]
        return final


if __name__ == '__main__':
    costs = [[30, 200], [10, 20], [30, 20], [400, 50]]
    res = Solution().twoCitySchedCost(costs)
    print(res)
