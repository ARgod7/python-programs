#  POST ORDER TRAVERSAL

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root: Optional[TreeNode]) -> list[int]:
        res = []
        def postorder(root):
            if not root:
                return
            res.append(root.val)
            postorder(root.left)
            postorder(root.right)
        postorder(root)
        return res