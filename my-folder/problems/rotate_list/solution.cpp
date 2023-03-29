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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr) return nullptr;
        ListNode* node = head;
        int l = 1;
        while (node->next) {
            l++;
            node = node->next;
        }
        node->next = head;

        int offset = (l-k%l);
        while(offset) {
            node = node->next;
            offset--;
        }
        head = node->next;
        node->next = nullptr;

        return head;
    }
};