# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1, t1, h2, t2 = None, None, None, None

        node = head
        while node:
            if node.val < x:
                if h1 is None:
                    h1 = t1 = node
                else:
                    t1.next = node
                    t1 = node
            else:
                if h2 is None:
                    h2 = t2 = node
                else:
                    t2.next = node
                    t2 = node
            node = node.next
        
        if h1 is None: return h2
        elif h2 is None: return h1
        t1.next = h2
        t2.next = None
        return h1