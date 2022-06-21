import queue
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bqueue = queue.PriorityQueue()
        ladQueue = queue.PriorityQueue()
        total = 0
        for i in range(len(heights) - 1):
            curr = heights[i]
            next = heights[i + 1]
            diff = next - curr
            if diff <= 0:
                pass
            else:
                if not bqueue.empty() and not ladQueue.empty():
                    bq = bqueue.get()
                    lq = ladQueue.get()
                    if bq[1] > lq:
                        bqueue.put((-lq, lq))
                        ladQueue.put(bq[1])
                        bricks += bq[1] - lq
                    else:
                        bqueue.put((-bq[1], bq[1]))
                        ladQueue.put(lq)

                if bricks >= diff:
                    bricks -= diff
                    bqueue.put((-diff, diff))
                elif ladders > 0:
                    ladders -= 1
                    ladQueue.put(diff)
                else:
                    break

            total += 1
        return total


if __name__ == '__main__':
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 2
    res = Solution().furthestBuilding(heights, bricks, ladders)
    print(res)
