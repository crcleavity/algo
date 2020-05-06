from typing import TypeVar, Generic, Generator, Optional

T = TypeVar("T")
class TreeNode(Generic[T]):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preorder():
    if root:
        yield root.val
        yield from preorder(root.left)
        yield from preorder(root.right)