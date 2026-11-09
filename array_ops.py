class ClassArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    # LIST (traverse)
    def list_all(self):
        if self.size == 0:
            print("Array is empty")
            return
        for i in range(self.size):
            print(f"[{i}] = {self.data[i]}")
        print()

    # INSERT at a position
    def insert(self, pos, value):
        if self.size == self.capacity:
            print("Array is full")
            return
        if pos < 0 or pos > self.size:
            print("Invalid position")
            return
        for i in range(self.size, pos, -1):   # shift right
            self.data[i] = self.data[i - 1]
        self.data[pos] = value
        self.size += 1

    # DELETE at a position
    def delete(self, pos):
        if pos < 0 or pos >= self.size:
            print("Invalid position")
            return None
        removed = self.data[pos]
        for i in range(pos, self.size - 1):   # shift left
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return removed

    # LINEAR SEARCH (works on unsorted data)
    def linear_search(self, key):
        for i in range(self.size):
            if self.data[i] == key:
                return i
        return -1

    # SORT (bubble sort, ascending)
    def sort(self):
        for i in range(self.size - 1):
            swapped = False
            for j in range(self.size - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            if not swapped:
                break

    # BINARY SEARCH (array must be sorted first)
    def binary_search(self, key):
        low, high = 0, self.size - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == key:
                return mid
            elif self.data[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# ---------- Test ----------
scores = ClassArray(10)
for s in [65, 82, 47, 91, 58, 74, 39, 88]:
    scores.insert(scores.size, s)           # add at the end

print("1. Original list:")
scores.list_all()

print("2. Linear search for 91 ->", scores.linear_search(91))   # 3

print("\n3. Insert 70 at position 2:")
scores.insert(2, 70)
scores.list_all()

print("4. Delete element at position 4:")
print("Removed:", scores.delete(4))          # 91
scores.list_all()

print("5. After sorting:")
scores.sort()
scores.list_all()

print("6. Binary search for 74 ->", scores.binary_search(74))   # 5
print("   Binary search for 100 ->", scores.binary_search(100)) # -1