from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixProduct = [0] * len(nums)
        product = []
        pp = 1
        sp = 1
        for i in range(len(nums)):
            j = len(nums) - i - 1
            sp *= nums[j]
            suffixProduct[j] = sp
        for i in range(len(nums)):
            c = pp
            if i + 1 < len(nums):
                c *= suffixProduct[i + 1]
            pp *= nums[i]
            product.append(c)
        return product

if __name__ == '__main__':
    arr = [1,2,3,4]
    res = Solution().productExceptSelf(arr)
    print(res)