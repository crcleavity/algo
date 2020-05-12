from collections import deque

class Graph:
    def __init__(self):
        super().__init__()
        self._num_vertics = num_vertics
        self._adjacency = [[] for _ in range(num_vertices)]
    
    def add_edge(self,s,t):
        