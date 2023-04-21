# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            node = head
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev, head
        
        # Cut

        node = head
        for _ in range(1, right):
            node = node.next
        seg_tail = node

        node = head if left > 1 else None
        for _ in range(2, left):
            node = node.next
        seg_head = node.next if node else head

        if node:
            node.next = None
        after_tail = seg_tail.next
        seg_tail.next = None
        seg_head, seg_tail = reverse(seg_head)

        # Join back
        seg_tail.next = after_tail
        if node:
            node.next = seg_head

        return head if left > 1 else seg_head
