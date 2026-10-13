# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        while n:
            if fast != None:
                fast = fast.next;
                n-=1
        if fast is None:
            return []
        while fast.next != None:
            slow = slow.next
            fast = fast.next    
        slow.next = slow.next.next;
        return dummy.next