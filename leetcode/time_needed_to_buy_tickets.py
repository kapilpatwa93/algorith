from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        l = len(tickets)
        for index in range(l):
            if tickets[index] < tickets[k]:
                total += tickets[index]
            else:
                if index < k:
                    total += tickets[k]
                elif index > k:
                    total += tickets[k] - 1
                else:
                    total += tickets[k]
        return total


def main():
    tickets = [1, 2, 3, 4]
    k = 2
    res = Solution().timeRequiredToBuy(tickets, k)
    print(res)


main()
