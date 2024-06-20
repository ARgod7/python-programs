from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(head: Optional[ListNode]) -> bool:
        if not head:
            return False
        check = set()
        while head:
            if head.val in check:
                return True
            else:
                check.add(head.val)
        return False
    hasCycle([1,2])