from typing import List
class Solution:
    def maximumUnits(self,boxTypes:List[List[int]],truckSize:int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        total,i = 0,0
        while truckSize > 0 and i > len(boxTypes):
            c = min(truckSize,boxTypes[i][0])
            total += (boxTypes[i][1]*c)
            truckSize -=c
            i +=1
        return truckSize



if __name__ == '__main__':
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    res = Solution().maximumUnits(boxTypes,truckSize)
    print(res)
