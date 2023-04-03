# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
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
    
    def is_equal(self, n1: Optional[ListNode], n2: Optional[ListNode]):
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        return n1 is None and n2 is None
    # def length(head: Optional[ListNode]):
    #     node = head
    #     l = 0
    #     while node:
    #         node = node.next
    #         l += 1
    #     return l
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = slow
        if fast:
            l2 = tail.next.next
        else:
            l2 = tail.next
        tail.next = None
        
        l1 = head
        l2 = self.reverse(l2)

        return self.is_equal(l1 ,l2)