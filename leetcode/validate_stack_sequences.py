from  typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        newList = []
        ini = 0
        while pushed[ini] != popped[0]:
            newList.append(pushed[ini])
            ini += 1
        newList.append(pushed[ini])
        ini += 1
        i = 0
        while i < len(popped):
            if len(newList) and newList[-1] == popped[i]:
                newList.pop()
                i = i + 1
            elif ini < len(pushed):
                newList.append(pushed[ini])
                ini += 1
            else:
                break
        return len(newList) == 0


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    res = Solution().validateStackSequences(pushed, popped)
    print(res)
