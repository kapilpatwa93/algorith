from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1 = 0
        p2 = len(people) - 1
        count = 0
        while p1 <= p2:
            if (people[p2] + people[p1]) <= limit:
                p2 -= 1
                p1 += 1
            else:
                p2 -= 1
            count += 1
        return count


if __name__ == '__main__':
    people = [1, 2, 4, 4, 2, 2, 4, 5, 6, 2]
    limit = 8
    res = Solution().numRescueBoats(people, limit)
    print(res)
