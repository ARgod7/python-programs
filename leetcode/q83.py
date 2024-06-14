from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
        


        # cur = head

        # while cur:
        #     while cur.next and cur.next.val == cur.val:
        #         cur.next = cur.next.next
        #     cur = cur.next
        # return head
        