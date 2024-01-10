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
    int getSize(ListNode* head) {
        int len = 0;
        while (head) {
            head = head->next;
            len++;
        }
        return len;
    }
    ListNode* deleteMiddle(ListNode* head) {
        int len = getSize(head);

        if (len == 1) {
            return nullptr;
        }

        int i=0;

        ListNode* prev = head;
        
        while (i<(len/2 - 1)) {
            prev = prev->next;
            i++;
        }

        prev->next = prev->next->next;

        return head;
    }
};