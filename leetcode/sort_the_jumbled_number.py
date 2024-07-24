from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        actualValue = dict()
        for i in range(len(mapping)):
            actualValue[i] = mapping[i]
        arr = [getValue(i,actualValue) for i in nums]
        final = [x for _, x in sorted(zip(arr, nums),key=lambda x:x[0])]
        return final


def getValue(num:int, actualMapping:dict[int]) -> int:
    value = 0
    for i in str(num):
        value = (value*10) + actualMapping[int(i)]
    return value


if __name__ == '__main__':
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = []
    res = Solution().sortJumbled(mapping, nums)
    print(res)