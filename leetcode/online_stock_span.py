class StockSpanner:
    stack = []
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while len(self.stack) > 0 and price >= self.stack[len(self.stack)-1][0]:
            ans += self.stack.pop()[1]
        self.stack.append((price,ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)