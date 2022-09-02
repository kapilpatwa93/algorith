from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        i = 0

        def moveAndShift(current: int, desired: int):
            c = people.pop(current)
            people.insert(desired, c)

        while i < len(people):
            h = people[i]
            moveAndShift(i, h[1])
            i += 1
        return people


if __name__ == '__main__':
    people = [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    res = Solution().reconstructQueue(people)
    print(res)
1,1,2,9,10