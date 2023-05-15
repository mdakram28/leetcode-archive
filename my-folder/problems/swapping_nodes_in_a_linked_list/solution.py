# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def ll_len(head):
            node = head
            i = 0
            while node is not None:
                node = node.next
                i += 1
            return i
        
        def ll_at(head, pos):
            node = head
            i = 0
            while i < pos:
                node = node.next
                i += 1
            return node

        l = ll_len(head)
        n1 = ll_at(head, k-1)
        n2 = ll_at(head, l-k)

        n1.val, n2.val = n2.val, n1.val

        return head



