/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *mergedHead, *mergedTail;
        if (!list1) {
            return list2;
        } else if(!list2) {
            return list1;
        } else if (list1->val < list2->val) {
            mergedHead = mergedTail = list1;
            list1 = list1->next;
        } else {
            mergedHead = mergedTail = list2;
            list2 = list2->next;
        }
        while(list1 && list2) {
            if (list1->val < list2->val) {
                mergedTail->next = list1;
                mergedTail = list1;
                list1 = list1->next;
            } else {
                mergedTail->next = list2;
                mergedTail = list2;
                list2 = list2->next;
            }
        }
        mergedTail->next = list1 ? list1 : (list2 ? list2 : nullptr);
        return mergedHead;
    }
};