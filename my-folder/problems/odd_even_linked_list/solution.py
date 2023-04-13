# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        

        odd_tail, odd_head = head, head
        even_tail, even_head = head.next, head.next

        node = head.next.next
        while node:
            odd_tail.next = node
            odd_tail = node
            node = node.next

            if node:
                even_tail.next = node
                even_tail = node
                node = node.next
        
        odd_tail.next = even_head
        even_tail.next = None
        return head