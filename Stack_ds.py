class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]


# Test
s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
print(s.is_full())    # True
s.push(40)            # Stack Overflow
print(s.peek())       # 30
print(s.pop())        # 30
print(s.pop())        # 20
print(s.is_empty())   # False
print(s.pop())        # 10
print(s.is_empty())   # True
s.pop()               # Stack Underflow