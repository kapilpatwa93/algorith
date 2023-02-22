from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = 0
        totalWeight = 0
        for i in weights:
            maxWeight = max(maxWeight, i)
            totalWeight += i

        start = maxWeight
        end = totalWeight

        def canShip(maxWeight: int) -> int:
            i, day = 0, 0
            while i < len(weights):
                dayWeight = 0
                while i < len(weights):
                    if (dayWeight + weights[i]) <= maxWeight:
                        dayWeight += weights[i]
                        i += 1
                    else:
                        break
                day += 1
            return day <= days

        minWeight = totalWeight
        while start <= end:
            mid = int((end + start) / 2)

            if canShip(mid):
                end = mid - 1
                minWeight = min(minWeight, mid)
            else:
                start = mid + 1

        return minWeight


if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # weights = [1, 2, 3, 1, 1]
    days = 5
    res = Solution().shipWithinDays(weights, days)
    print(res)
