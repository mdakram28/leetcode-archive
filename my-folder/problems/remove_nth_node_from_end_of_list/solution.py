# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        st = []
        node = head
        while node:
            st.append(node)
            node = node.next

        if n == len(st):
            return head.next
        else:
            st[-(n+1)].next = st[-n].next
            return head