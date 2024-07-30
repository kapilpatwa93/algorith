from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        smallArr = [0 for _ in range(len(rating))]
        greatArr = [0 for _ in range(len(rating))]

        for i in range(len(rating)):
            smallCount = 0
            greatCount = 0
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    smallCount += 1
                if rating[j] > rating[i]:
                    greatCount += 1
                smallArr[i] = smallCount
                greatArr[i] = greatCount
        total = 0
        print(smallArr,greatArr)
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    total = total + smallArr[j]
                if rating[j] > rating[i]:
                    total = total + greatArr[j]


        return total




if __name__ == '__main__':
    rating = [2,5,4,3,1]
    res = Solution().numTeams(rating)
    print(res)