# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        return max(vals[i]+vals[-i-1] for i in range(len(vals)//2))