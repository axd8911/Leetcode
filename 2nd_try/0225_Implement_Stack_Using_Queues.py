class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = collections.deque([])



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.s1)-1):
            self.s1.append(self.s1.popleft())
        return self.s1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(len(self.s1)-1):
            self.s1.append(self.s1.popleft())
        res = self.s1.popleft()
        self.s1.append(res)
        return res


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.s1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
