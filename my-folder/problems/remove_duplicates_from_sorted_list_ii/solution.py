# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = collections.defaultdict(int)
        node = head
        while node:
            f[node.val] += 1
            node = node.next
        
        include = sorted(k for k, v in f.items() if v == 1)
        
        head = ListNode()
        prev = None
        tail = head
        for val in include:
            tail.val = val
            tail.next = ListNode()
            prev = tail
            tail = tail.next
        
        if prev is None:
            return None
        else:
            prev.next = None
            return head