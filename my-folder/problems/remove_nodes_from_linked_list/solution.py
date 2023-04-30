# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def get_next(head):
        if head.next is None:
            return head
        next_node = self.removeNodes(head.next)
        if head.val >= next_node.val:
            head.next = next_node
            return head
        else:
            return next_node