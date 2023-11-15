# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        at = head
        while at and at.next:
            at.next, at = ListNode(math.gcd(at.val, at.next.val), at.next), at.next
        return head