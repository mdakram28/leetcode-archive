# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        prev = None
        node = head
        while node:
            next_node = node.next
            if node.val == val:
                prev.next = next_node
            else:
                prev = node
            node = next_node
        
        return head