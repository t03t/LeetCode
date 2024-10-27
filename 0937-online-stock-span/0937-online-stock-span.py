class StockSpanner:
    # Span = maximum number of consecutive days in which stock_pice was less than or equal to the price of that day

    def __init__(self):
        self.mono_stack = []
        
    def next(self, price: int) -> int:
        res = 1
        while self.mono_stack and price >= self.mono_stack[-1][0]:
            res += self.mono_stack[-1][1]
            self.mono_stack.pop()
        self.mono_stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)