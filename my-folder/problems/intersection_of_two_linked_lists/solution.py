# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node):
            count = 0
            while node is not None:
                count += 1
                node = node.next
            return count
        

        lengthA = length(headA)
        lengthB = length(headB)

        if lengthB > lengthA:
            lengthA, lengthB = lengthB, lengthA
            headA, headB = headB, headA
        
        skipA = lengthA - lengthB

        while skipA > 0 and headA is not None:
            headA = headA.next
            skipA -= 1
        
        while headA != headB and headA is not None and headB is not None:
            headA = headA.next
            headB = headB.next
        
        return headA if headA == headB else None
