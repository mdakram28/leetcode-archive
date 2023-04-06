# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        head = head.next or head

        while node and node.next:
            n1, n2 = node, node.next
            node = n2.next

            if n2.next and n2.next.next:
                n1.next = n2.next.next
            else:
                n1.next = n2.next
            
            n2.next = n1

        return head
            