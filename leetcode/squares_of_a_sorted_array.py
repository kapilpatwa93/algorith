from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        def firstPosNumberIndex() -> int:
            firstPosIndex = len(nums)
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = int((start + end) / 2)
                if nums[mid] < 0:
                    start = mid + 1
                else:
                    firstPosIndex = mid
                    end = mid - 1

            return firstPosIndex

        def getSmallerNumberIndex(negIndex, posIndex) -> int:
            if negIndex < 0 and posIndex >= len(nums):
                return -1
            if negIndex < 0:
                return posIndex
            elif posIndex >= len(nums):
                return negIndex
            return negIndex if abs(nums[negIndex]) < abs(nums[posIndex]) else posIndex

        arr = []

        posIndex = firstPosNumberIndex()
        negIndex = posIndex - 1

        while True:
            index = getSmallerNumberIndex(negIndex, posIndex)
            if index == -1:
                break
            if index == negIndex:
                arr.append(nums[index] * nums[index])
                negIndex -= 1
            else:
                arr.append(nums[index] * nums[index])
                posIndex += 1
        return arr


def main():
    nums = [-4, -1, 0, 3, 10]
    res = Solution().sortedSquares(nums)
    print(res)


main()
