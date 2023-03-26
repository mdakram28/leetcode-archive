# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def get_min():
            min_i = -1
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if min_i == -1 or lists[i].val < lists[min_i].val:
                    min_i = i
            return min_i

        min_i = get_min()
        if min_i == -1:
            return None
        head = lists[min_i]
        tail = head
        lists[min_i] = head.next

        while (min_i := get_min()) >= 0:
            tail.next = lists[min_i]
            tail = tail.next
            lists[min_i] = tail.next
        
        tail.next = None

        return head
