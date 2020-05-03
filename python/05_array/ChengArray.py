class ChengArray:
    def __init__(self, capacity:int):
        self._data = []
        self._capacity = capacity
    
    def __getitem__(self, position:int)->object:
        return self._data[position]
    
    def __setitem__(self, position:int,number:object):
        self._data[position] = number
    
    def __len__(self):
        return len(self._data)

    def find(self,index:int):
        try:
            return self._data[index]
        except IndexError:
            return None
    
    def delete(self, index:int):
        try:
            self._data[index].pop()
            return True
        except IndexError:
            return False
    
    def insert(self, index:int, value:int):
        if(len(self._data) >= self._capacity):
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for item in self:
            print(item)
    
def test():
    array = ChengArray(10)
    array.insert(0,3)
    array.insert(0,4)
    array.insert(6,7)
    array.print_all()

if __name__ == "__main__":
    test()