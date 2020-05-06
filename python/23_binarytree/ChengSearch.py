from queue import Queue
import math

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self, val_list = []):
        super().__init__()
        self.root = None
        for n in val_list:
            self.insert(n)
    
    def insert(self, data):
        assert(isinstance(data, int))
        
        if self.root is None:
            self.root = TreeNode(data)
        else:
            n = self.root
            while n:
                p = n
                if data < n.val:
                    n = n.left
                else:
                    n = n.right
            new_node = TreeNode(data)
            new_node.parent = p
            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node
        return True
    

    def search(self, data):
        ret = []

        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    ret.append(n)
                n = n.right
        return ret
    
    def delete(self, data):
        assert(isinstance(data, int))

        del_list = self.search(data)

        for n in del_list:
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)
    
    def _del(self, node):
        #1
        if node.left == None and node.right == None:
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None
        #2
        elif node.left == None and node.right != None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val > node.parent.val:
                    node.parent.right = node.right
                else:
                    node.parent.left = node.right
                node.parent = None
                node.right = None
                node.right.parent = node.parent
        elif node.left != None and node.right == None:
            if node == self.root:
                self.root = node.left
                node.left.parent = None
                node.left = None
            else:
                if node.val > node.parent.val:
                    node.parent.right = node.left
                else:
                    node.parent.left = node.left
                node.parent = None
                node.left = None
                node.left.parent = node.parent
        #3
        else:
            min_node = node.right
            if min_node.left:
                min_node = min_node.left

            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
            
        def get_min(self):
            if self.root == None:
                return None
            n = self.root
            while n.left:
                n = n.left
            return n.val                

        def get_max(self):
            if self.root == None:
                return None
            n = self.root
            while n.right:
                n = n.right
            return n.val
        
        def in_order(self):
            if node is None:
                return []
            
            ret = []
            n = node
            ret.extend(self.in_order(n.left))
            ret.append(n.val)
            ret.extend(self.in_order(n.right))

        def __repr__(self):
            print(str(self.in_order()))
            return self._draw_tree()
        
        def _bfs(self):
            if self.root is None:
                return []

            ret = []
            q = Queue()
            q.put((self.root, 1))

            while not q.empty():
                first = q.get()
                if first[0] is not None:
                    ret.append((n[0].val,n[1]))
                    q.put((n[0].left, n[1]*2))
                    q.put((n[0].right, n[1]*2+1))
            
            return ret
        
        def _draw_tree(self):
            nodes = self._bfs()

            if not nodes:
                print("This tree has no nodes")
                return
            layer_num = int(math.log(nodes[-1][1],2)) + 1
            prt_nums = []

            for i in range(layer_num):
                prt_nums.append([None]*2**i)
            
            for v, p in nodes:
                row = int(math.log(p,2))
                col = p % 2**row
                prt_nums[row][col] = v
 
            prt_str = ''
            for l in prt_nums:
                plt_str += str(l)[1:-1] + '\n'
            return prt_str