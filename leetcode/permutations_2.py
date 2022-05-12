from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        total = len(nums)
        nums.sort()

        def recurse(arr: List[int], arr2: List[int]):

            if len(arr) == total:
                res.append(arr)
                return
            prev = None
            for i in range(len(arr2)):
                if prev != arr2[i]:
                    newArr2 = arr2.copy()

                    newArr = arr.copy()
                    newArr.append(newArr2.pop(i))
                    recurse(newArr, newArr2)
                prev = arr2[i]

        recurse([], nums)
        return res


if __name__ == '__main__':
    nums = [3, 3, 0, 3]
    res = Solution().permuteUnique(nums)
    print(res)
