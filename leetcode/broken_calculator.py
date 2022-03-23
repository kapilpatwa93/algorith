class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target != startValue:
            if target > startValue:
                if target % 2 == 1:
                    target += 1
                else:
                    target = int(target / 2)
                count += 1
            elif target < startValue:
                count += startValue - target
                target = startValue
        return count


if __name__ == '__main__':
    startValue = 3
    target = 97
    res = Solution().brokenCalc(startValue, target)
    print(res)
