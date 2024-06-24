from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # pre = None
        # while slow:
        #     temp = slow.next
        #     slow.next = pre
        #     pre = slow
        #     slow = temp

        # l , r = head, pre
        # while r:
        #     if l.val != r.val:
        #         return False
        #     l = l.next
        #     r = r.next
        # return True 
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        l , r = 0 , len(arr)-1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

isPalindrome([1,2,2,1])
        
