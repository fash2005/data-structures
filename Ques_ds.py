class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]


# Test
q = Queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.is_full())    # True
q.enqueue(40)         # Queue Overflow
print(q.peek())       # 10
print(q.dequeue())    # 10
print(q.dequeue())    # 20
print(q.is_empty())   # False
print(q.dequeue())    # 30
print(q.is_empty())   # True