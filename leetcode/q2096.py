# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # def dfs(node,path,target):
        #     if not node:
        #         return False
        #     if node.val == target:
        #         return path
        #     path.append('L')
        #     res = dfs(node.left,path,target)
        #     if res: return res
        #     path.pop()
        #     path.append('R')
        #     res = dfs(node.right,path,target)
        #     if res: return res
        #     path.pop()
        #     return ""
        # start_path = dfs(root,[],startValue)
        # dest_path = dfs(root,[],destValue)
        # i = 0
        # while i < min(len(start_path),len(dest_path)):
        #     if start_path[i] != dest_path[i]:
        #         break
        #     i += 1
        # res = ['U'] * len(start_path[i:]) + dest_path[i:]
        # return "".join(res)
        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False
        p1 = []
        p2 = []
        find(root, startValue, p1)
        find = find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return 'U' * len(p1) + ''.join(p2[::-1])
        