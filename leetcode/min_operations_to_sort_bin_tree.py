# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    matrix = []
    minOperations = 0
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        self.matrix = []
        self.minOperations = 0
        def findMinSwap(arr: List[int]) -> int:
            posMap = { arr[i] : i for i in range(len(arr))}
            sortedArr = sorted(arr)
            count = 0
            for i in range(len(arr)):
                if arr[i] != sortedArr[i]:
                    count +=1
                    curr = arr[i]
                    desiredLocation = posMap[sortedArr[i]]
                    arr[desiredLocation],arr[i] = arr[i],arr[desiredLocation]
                    posMap[sortedArr[i]] = i
                    posMap[curr] = desiredLocation
                    # print('arr',desiredLocation, i, arr)
            # print(count)
            return count



        def traverse(root:Optional[TreeNode], level):
            if root is None:
                return
            if len(self.matrix) <= level:
                self.matrix.append([])
            self.matrix[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        traverse(root,0)
        # print(self.matrix)
        totalCount = 0
        for i in self.matrix:
            totalCount += findMinSwap(i)

        print(totalCount)
        return totalCount

def getTree(nodes: List[int]) -> TreeNode:
    def recurse(index):
        if index >= len(nodes):
            return None
        if nodes[index] is None:
            return None
        subroot = TreeNode(nodes[index])
        left = recurse((index * 2) + 1)
        right = recurse((index * 2) + 2)
        subroot.left = left
        subroot.right = right
        return subroot

    return recurse(0)


if __name__ == '__main__':
    list = [1, 4,3, 7, 6, 8, 5, 7, None, None, None, None, 9, 8, None, None]
    tree = getTree(list)
    Solution().minimumOperations(tree)
    print(tree)
