class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min is None or val < current_min:
            current_min = val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


class MinStackMain:
    obj = MinStack()
    obj.push(3)
    print(obj.top())
    print(obj.getMin())
    obj.push(4)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
