from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            if a < 0:
                equal = False
                while len(s) > 0:
                    top = s[len(s) - 1]
                    if top < 0:
                        s.append(a)
                        break
                    if abs(a) >= top:
                        s.pop()
                    if abs(a) == top:
                        equal = True
                        break
                    if abs(a) < top:
                        break
                if len(s) == 0 and not equal:
                    s.append(a)
            else:
                s.append(a)
        return s


if __name__ == '__main__':
    asteroids = [1, 2, -3]
    res = Solution().asteroidCollision(asteroids)
    print(res)
