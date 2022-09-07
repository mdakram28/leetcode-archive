/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head) return nullptr;
        ListNode *n1 = head; 
        ListNode *n2 = head;
        while(n2->next && n2->next->next) {
            n1 = n1->next;
            n2 = n2->next->next;
            if(n1 == n2) {
                while(head!=n1) {
                    head = head->next;
                    n1 = n1->next;
                }
                return head;
            }
        }
        return nullptr;
    }
};