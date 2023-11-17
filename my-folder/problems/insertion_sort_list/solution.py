# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None

        def to_str(node: Optional[ListNode]):
            if node is None:
                return "None"
            ret = ""
            while node is not None:
                ret += f"{node.val} -> "
                node = node.next
            ret += "None"
            return ret

        def insert_in_sorted(node: ListNode):
            nonlocal newhead
            # print("Inserting", node.val)
            # print("Before", to_str(newhead))
            if newhead is None:
                newhead = node
            elif node.val <= newhead.val:
                node.next = newhead
                newhead = node
            else:
                prevnode = newhead
                while prevnode.next is not None and prevnode.next.val < node.val:
                    prevnode = prevnode.next
                prevnode.next, node.next = node, prevnode.next
            # print("After", to_str(newhead))
            
        

        node = head
        while node is not None:
            nextnode = node.next
            node.next = None
            insert_in_sorted(node)
            node = nextnode
        
        return newhead