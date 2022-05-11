class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1] * 5
        sum = 5
        for i in range(n - 1):
            newArr = [sum] * 5
            newSum = sum
            for x in range(len(arr) - 1):
                sum = sum - arr[x]
                newSum += sum
                newArr[x + 1] = sum
            arr = newArr
            sum = newSum

        return sum


if __name__ == '__main__':
    n = 33
    res = Solution().countVowelStrings(n)
    print(res)
