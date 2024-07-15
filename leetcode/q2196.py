from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for par, child, left in descriptions:
            children.add(child)
            if par not in nodes:
                nodes[par] = TreeNode(par)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if left:
                nodes[par].left = nodes[child]
            else:
                nodes[par].right = nodes[child]
        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]
    createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])


        