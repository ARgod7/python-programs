# SYMETRIC TREE

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l , r):
            if not l and not r:
                return 1
            if not l or not r:
                return 0
            if (l.val == r.val and dfs(l.left , r.right) and dfs(l.right , r.left)):
                return 1
            return 0
        return dfs(root.left,root.right)
        