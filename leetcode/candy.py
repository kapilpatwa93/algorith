from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = 1
        for i in reversed(range(0, len(ratings) - 1)):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i + 1] + 1, candies[i])

        return sum(candies)


if __name__ == '__main__':
    ratings = [4, 3, 3, 2, 1, 2, 3, 1, 2, 3,3, 2, 1]
    res = Solution().candy(ratings)
    print(res)
