import functools
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        def moveAndShift(current: int, moveTo: int):
            for i in reversed(range(moveTo + 1, current + 1)):
                people[i], people[i - 1] = people[i - 1], people[i]

        def compare(key1, key2):
            if key1[0] > key2[0]:
                return 1
            elif key1[0] < key2[0]:
                return -1
            else:
                if key1[1] > key2[1]:
                    return -1
                elif key1[1] < key2[1]:
                    return 1
                return 0

        people.sort(key=functools.cmp_to_key(compare), reverse=True)
        for i in range(len(people)):
            if i > people[i][1]:
                moveAndShift(i, people[i][1])
        return people


if __name__ == '__main__':
    people = [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    res = Solution().reconstructQueue(people)
    print(res)
