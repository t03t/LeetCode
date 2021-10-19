class MinStack(object):

    def __init__(self):
        self.size = 0
        self.stack = []
        self.smallest= []
        self.stop =0
        self.first = True

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.smallest or val<=self.smallest[-1]:
            self.smallest.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1]==self.smallest[-1]:
            self.smallest.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.smallest[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()