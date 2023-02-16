from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def createTree():
            treeMap = {}
            for i in range(len(manager)):
                if manager[i] == -1:
                    continue
                if manager[i] in treeMap:
                    treeMap[manager[i]].append(i)
                else:
                    treeMap[manager[i]] = [i]
            return treeMap

        def setInformTime(arr: List[int], time: int):
            for i in arr:
                finalTime[i] = time
                queue.append(i)

        i = 0
        queue = [headID]
        finalTime = [0] * len(informTime)
        maxTime = 0
        treeMap = createTree()

        while i < len(queue):
            if queue[i] in treeMap:
                item = queue[i]
                setInformTime(treeMap[item], informTime[item] + finalTime[item])
                maxTime = max(maxTime, informTime[item] + finalTime[item])
            i += 1
        return maxTime


if __name__ == '__main__':
    n = 13
    headID = 2
    manager = [2, 2, -1, 2, 2, 3, 1, 4, 1, 1, 0, 3, 3, 9]
    informTime = [1, 1, 3, 2, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0]
    res = Solution().numOfMinutes(n, headID, manager, informTime)
    print(res)
