# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def sort(l , r):
            if l > r:
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = sort(l , m-1)
            root.right = sort(m+1 , r)
            return root
        return sort(0, len(nums)-1)
    # if len(nums) == 0:
        #     return None
        # m = len(nums)//2
        # curNode = TreeNode(nums[m],None,None)
        # curNode.left = self.sortedArrayToBST(nums[0:m])
        # curNode.right = self.sortedArrayToBST(nums[m+1:])
        # return curNode