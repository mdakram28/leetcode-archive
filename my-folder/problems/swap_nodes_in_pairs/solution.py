# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = None if head is None else (head if head.next is None else head.next)

        prev = None
        while head is not None and head.next is not None:
            mid = head.next
            if prev is not None:
                prev.next = mid
            head.next = head.next.next
            mid.next = head

            prev = head
            head = head.next
        
        return ret_head

            