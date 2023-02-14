from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = [arr[0]]
        for i in range(1, len(arr)):
            prefixSum.append(prefixSum[i - 1] + arr[i])
        total = 0
        even = 0
        odd = 0
        for i in range(len(prefixSum)):
            if prefixSum[i] % 2 == 1:
                total += 1
                odd += 1
                total += even
            else:
                even += 1
                total += odd

        return total % (pow(10, 9) + 7)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = Solution().numOfSubarrays(nums)
    print(res)
