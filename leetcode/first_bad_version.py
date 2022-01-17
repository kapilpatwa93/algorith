# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        firstBadVersion = 0
        while start <= end:
            mid = int((start + end) / 2)
            if not isBadVersion(mid):
                start = mid + 1
            else:
                lastBadVersion = mid
                end = mid - 1
        return firstBadVersion