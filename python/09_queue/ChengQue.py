


class ArrayQueue:
    def __init__(self,capacity):
        super().__init__()
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item):
        if self._tail == self._head:
            return False
        else:
            for i in range(0, self._tail - self._head):
                self._items[i] = self._items[i+self._head]
            self._tail = self._tail - self._head
            self._head = 0
        
        self._items.insert(self._tail,item)
        self._tail += 1
        return True
    
    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None
    
    def __repr__(self):
        return " ".join(item for item in self._items[self._head:self._tail])

    def enqueue(self, item):
        if self._tail == self._capacity:
            return False
        else:
            for i in range(0, self._tail - self._head):
                self._items[i] = self.items[i + self.head]
            self._tail = self._tail - self._head
            self._head = 0
        
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
