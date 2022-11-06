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
    ListNode* reverseGroup(ListNode* first, ListNode* afterLast) {
        ListNode* next;
        ListNode* last = afterLast;
        while (first != afterLast) {
            next = first->next;
            first->next = last;
            last = first;
            first = next;
        }
        return last;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* newHead = head;
        ListNode* beforeFirst = nullptr;
        ListNode* first = head;
        ListNode* node = first;
        int i=0;
        while (node != nullptr) {
            node = node->next;
            i++;
            if (i == k) {
                i=0;
                ListNode* newFirst = reverseGroup(first, node);
                if (first == head) {
                    newHead = newFirst;
                }
                if (beforeFirst != nullptr) {
                    beforeFirst->next = newFirst;
                }
                beforeFirst = first;
                first = node;
            }
        }
        return newHead;
    }
};