class CircularQueue:
    def __init__(self,capacity):
        self._items = []
        self._head = 0
        self._tail = 0
        self._capacity = capacity

    def enqueue(self, item):
        if (self._tail + 1)%self._capacity == self._head:
            return False
        
        self._items.append(item)
        self._tail = (self._tail+1) % self._capacity
        return True
    
    def dequeue(self):
        if self._head == self._tail:
            return False
        
        item = self._items[self._head]
        self._head = (self._head+1) % self._capacity
        return item
    
    