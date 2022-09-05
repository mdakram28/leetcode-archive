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
    ListNode* reverseList(ListNode* head) {
        vector<ListNode *> nodes;
        nodes.push_back(nullptr);
        while(head) {
            nodes.push_back(head);
            head = head->next;
        }
        int size = nodes.size();
        for(int i=size-1;i>0;i--) {
            nodes[i]->next = nodes[i-1];
        }
        return nodes[size-1];
    }
};