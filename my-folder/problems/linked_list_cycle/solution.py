# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        n1 = head
        n2 = head.next.next

        while n1 != n2:
            if n2 is None or n2.next is None:
                return False
            n1 = n1.next
            n2 = n2.next.next
        
        return True