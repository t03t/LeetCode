import collections

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.dq = collections.deque()  
        self.running_sum = 0          

    def next(self, val: int) -> float:
        self.dq.append(val)
        self.running_sum += val
        if len(self.dq) > self.size:
            oldest = self.dq.popleft()
            self.running_sum -= oldest
        return self.running_sum / len(self.dq)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)