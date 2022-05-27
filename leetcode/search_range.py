from typing import List


class Solution:
    l = -1
    r = -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.l = -1
        self.r = -1
        length = len(nums)

        def search(lstart, lend, rstart, rend):
            lmid = int((lend - lstart) / 2)
            rmid = rstart + int((rend - rstart) / 2)
            # if rstart >= length -1 and lend <= 0:
            #     return

            if lmid >= 0 and lmid < length and nums[lmid] == target:
                self.l = lmid
                lstart = 0
                lend = lmid - 1
            if rmid >= 0 and rmid < length and nums[rmid] == target:
                self.r = rmid
                rstart = rmid + 1
                rend = length - 1
            if rmid >= length - 1 and lmid <= 0:
                    return
            search(lstart, lend, rstart, rend)

        search(0, length, 0, length)
        return [self.l, self.r]


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 2, 2]
    target = 2
    res = Solution().searchRange(nums, 2)
    print(res)
