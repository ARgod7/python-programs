# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0
        def dfs(node):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count
            
            ld = dfs(node.left)
            rd = dfs(node.right)

            for d1 in ld:
                for d2 in rd:
                    if d1 + d2 <= distance:
                        self.pairs += ld[d1] * rd[d2]
            
            alldist = defaultdict(int)
            for d in ld:
                if d + 1 <= distance:
                    alldist[d + 1] = ld[d]
            for d in rd:
                if d + 1 <= distance:
                    alldist[d + 1] += rd[d]
            return alldist
        dfs(root)
        return self.pairs