# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            while  curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr
            prev = curr
            curr = curr.next

        return dummy.next            