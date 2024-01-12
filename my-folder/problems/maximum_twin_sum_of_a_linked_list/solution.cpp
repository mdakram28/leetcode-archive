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
    int getLength(ListNode* node) {
        int l = 0;
        while(node) {
            node = node->next;
            l++;
        }
        return l;
    }

    ListNode* move(ListNode* node, int n) {
        for(int i=0; i<n; i++) {
            node = node->next;
        }
        return node;
    }

    ListNode* reverse(ListNode* head) {
        ListNode* node = head;
        ListNode* prevNode = nullptr;

        while (node) {
            auto next = node->next;
            node->next = prevNode;
            prevNode = node;
            node = next;
        }

        return prevNode;
    }

    int pairSum(ListNode* head) {
        const int n = getLength(head);

        auto mid = move(head, n/2 - 1);
        auto afterMid = reverse(mid->next);
        mid->next = nullptr;

        int ans = 0;
        auto n1 = head;
        auto n2 = afterMid;
        while(n1) {
            ans = std::max(ans, n1->val + n2->val);
            n1 = n1->next;
            n2 = n2->next;
        }
        return ans;
    }
};