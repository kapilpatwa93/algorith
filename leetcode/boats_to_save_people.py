from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        count = 0
        while start <= end:
            if people[end] + people[start] <= limit:
                start += 1
            end -= 1
            count += 1
        return count


if __name__ == '__main__':
    people = [1, 2, 4, 4, 2, 2, 4, 5, 6, 2]
    limit = 8
    res = Solution().numRescueBoats(people, limit)
    print(res)
