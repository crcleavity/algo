from typing import Optional

class Node:
    def __init__(self,data,next=None):
        super().__init__()
        self._data = data
        self._next = next

class LinkedStack:

    def __init__(self):
        super().__init__()
        self._top = None
    
    def push(self,value):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top
    
    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value
        
    def __repr__(self):
        return super().__repr__()
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join(f"{num}]" for num in nums)
    
    
