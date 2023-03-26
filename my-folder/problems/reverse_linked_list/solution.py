# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        
        if len(nodes) == 0:
            return None
        head = nodes.pop()
        tail = head
        while len(nodes) > 0:
            node = nodes.pop()
            tail.next = node
            tail = node
        tail.next = None

        return head
