from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = [set() for _ in range(n)]
        visited = [False] * n

        if len(connections) < (n - 1):
            return -1

        for c in connections:
            m[c[0]].add(c[1])
            m[c[1]].add(c[0])

        def traverse(node):
            queue = [node]
            i = 0
            while i < len(queue):

                currNode = queue[i]
                if not visited[currNode]:
                    visited[currNode] = True
                    for j in m[currNode]:
                        queue.append(j)
                i += 1

        count = 0
        for node in range(len(m)):
            if not visited[node]:
                traverse(node)
                count += 1
        return count - 1


if __name__ == '__main__':
    n = 7
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 6]]
    res = Solution().makeConnected(n, connections)
    print(res)
