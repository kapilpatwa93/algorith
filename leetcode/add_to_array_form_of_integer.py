from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = k
        i = len(num) - 1
        arr = []
        carry = 0
        while n > 0 or i >= 0:
            n = int(n / 10)
            sum = (n % 10) + (num[i] if i >= 0 else 0) + carry
            carry = int(sum / 10)
            sum = sum % 10
            arr.insert(0, sum)
            i -= 1
        if carry > 0:
            arr.insert(0, carry)
        return arr


if __name__ == '__main__':
    num = [1, 2, 3, 4]
    k = 100
    res = Solution().addToArrayForm(num, k)
    print(res)
