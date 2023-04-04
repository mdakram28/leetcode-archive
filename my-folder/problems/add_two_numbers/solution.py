# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h2 = l2
        carry = 0
        head = l1
        tail = None
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s//10
            l1.val = s%10
            tail = l1
            l1 = l1.next
            l2 = l2.next
        
        l = l1 if l1 else l2
        tail.next = l
        while l:
            s = l.val + carry
            carry = s//10
            l.val = s%10
            tail = l
            l = l.next
        if carry:
            tail.next = h2
            tail = h2
            tail.val = carry
            tail.next = None
        return head
