from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxAmount = 0
        for cust in accounts:
            total = 0
            for amount in cust:
                total += amount
            maxAmount = max(maxAmount, total)
        return maxAmount


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    res = Solution().maximumWealth(accounts)
    print(res)
