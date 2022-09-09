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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *origHead = head;
        ListNode *node = head;
        for(int i=0;i<n;i++) {
            node = node->next;
        }
        if(!node) {
            return head->next;
        }
        node = node->next;
        while(node) {
            head = head->next;
            node = node->next;
        }
        head->next = head->next->next;
        return origHead;
    }
};