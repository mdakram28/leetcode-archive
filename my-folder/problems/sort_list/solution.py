# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid(head):
            if head is None:
                return None
            slow = head
            fast = head.next
            while fast is not None and fast.next is not None:
                slow  = slow.next
                fast = fast.next.next
            return slow
        
        def merge(n1, n2):
            head = None
            tail = None
            if n1 is None and n2 is None:
                return None
            elif n1 is None or n2 is None:
                return n1 or n2
            
            if n1.val < n2.val:
                head = n1
                n1 = n1.next
            else:
                head = n2
                n2 = n2.next
            tail = head

            while n1 is not None and n2 is not None:
                if n1.val < n2.val:
                    tail.next = n1
                    n1 = n1.next
                else:
                    tail.next = n2
                    n2 = n2.next
                tail = tail.next
            
            tail.next = n1 or n2
            return head


        if head is None:
            return None
        
        l1 = head
        l1_tail = get_mid(head)
        l2 = l1_tail.next
        l1_tail.next = None

        if l2 is None:
            return l1

        # print(f"l1 = {l1.val}, l2 = {l2.val}")

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        return merge(l1, l2)