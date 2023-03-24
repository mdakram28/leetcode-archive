# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def print_ll():
            node = head
            while node is not None:
                print(f"{node.val} -> ", end="")
                node = node.next
            print("END")
        
        if head.next is None or head.next.next is None:
            return head

        # Get the length of list
        n1, n2 = head, head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next

        # print(f"{n1.val=}, {n2.val=}")
        # Make a list of alternate nodes with length = len/2
        mid = n1
        tails = []
        node = head
        n1 = n1.next
        mid.next = None
        while n1 is not None:
            tails.append(n1)
            n1 = n1.next
        
        # travrse the nodes putting one from the end of alternate nodes 
        # Stop when nextNode is None or next.next node is None
        # print_ll()
        node = head
        while len(tails) > 0:
            temp = node.next
            mid_node = tails.pop()
            node.next = mid_node
            mid_node.next = temp

            node = temp
            # print_ll()
        
