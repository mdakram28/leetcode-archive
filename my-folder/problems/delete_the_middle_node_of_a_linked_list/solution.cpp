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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* node = head;
        int n=0;
        while (node) {
            n++;
            node = node->next;
        }
        n /= 2;
        n--;
        if (n==-1) return head->next;

        node = head;
        while(n) {
            node = node->next;
            n--;
        }
        node->next = node->next->next;
        return head;
    }
};