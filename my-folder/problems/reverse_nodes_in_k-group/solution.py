# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def cut_next_segment():
            nonlocal old_head
            segment_head = old_head
            node = old_head
            i = 1
            while node is not None and i<k:
                node = node.next
                i += 1
            if node:
                old_head = node.next
                node.next = None
                return segment_head, node
            else:
                return None, None
        
        def reverse(head):
            if head is None:
                return None
            prev = None
            node = head
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
                

        old_head = head
        new_head = None
        new_tail = None
        
        while True:
            # Cut segment from old list
            segment_head, segment_tail = cut_next_segment()
            if segment_head is None:
                if new_tail is not None:
                    new_tail.next = old_head
                break
            
            # Reverse Segment
            reverse(segment_head)
            segment_head, segment_tail = segment_tail, segment_head

            # Attack segment to new list
            if new_tail is None:
                new_head = segment_head
                new_tail = segment_tail
            else:
                new_tail.next = segment_head
                new_tail = segment_tail
        
        return new_head
            


