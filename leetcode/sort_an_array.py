from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1: List[int], arr2: List[int]):
            merged = []
            i = 0
            j = 0
            counter = 0
            while counter < (len(arr1) + len(arr2)):
                if i >= len(arr1):
                    merged.append(arr2[j])
                    j += 1
                elif j >= len(arr2):
                    merged.append(arr1[i])
                    i += 1
                elif arr1[i] > arr2[j]:
                    merged.append(arr2[j])
                    j += 1
                else:
                    merged.append(arr1[i])
                    i += 1
                counter += 1
            return merged

        def mergeSort(nums: List[int]) -> List[int]:
            if len(nums) > 2:
                mid = int(len(nums) / 2)
                arr1 = mergeSort(nums[:mid])
                arr2 = mergeSort(nums[mid:])
                merged = merge(arr1, arr2)
                return merged

            if len(nums) == 2 and nums[0] > nums[1]:
                return [nums[1], nums[0]]
            return nums

        return mergeSort(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = Solution().sortArray(nums)
    print(res)
