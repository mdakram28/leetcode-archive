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
    ListNode* deleteDuplicates(ListNode* head) {
        map<int, int> f;
        ListNode* node = head;
        while(node) {
            f[node->val]++;
            node = node->next;
        }

        node = head;
        while(node && f[node->val] > 1) {
            node = node->next;
        }
        head = node;
        ListNode* prev = node;
        if (node) node = node->next;
        while (node) {
            if (f[node->val] > 1) {
                prev->next = node->next;
            } else {
                prev = node;
            }
            node = node->next;
        }
        return head;
    }
};