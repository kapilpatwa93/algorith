from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        maxI = 0
        for i in range(1, len(values)):

            max_score = max(max_score, values[maxI] + values[i] - i + maxI)
            if values[maxI] < (values[i] + (i - maxI)):
                maxI = i
        return max_score


if __name__ == '__main__':
    values = [15, 1, 8, 2, 20]
    res = Solution().maxScoreSightseeingPair(values)
    print(res)
