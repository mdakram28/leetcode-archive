#ifdef LOCAL_RUN

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#endif
// Solution Begin ----------
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry = 0;
        int sum;
        ListNode *ret = l1;
        bool l2_finished = false;
        while (true) {

            if (l2_finished) {
                sum = l1->val + carry;
                l1->val = sum % 10;
                carry = sum / 10;

                if (l1->next == nullptr) {
                    break;
                }
                l1 = l1->next;
            } else {
                sum = l1->val + l2->val + carry;
                l1->val = sum % 10;
                carry = sum / 10;

                if (l1->next == nullptr) {
                    if (l2->next == nullptr) {
                        break;
                    } else {
                        l1->next = l2->next;
                        l2->next = nullptr;
                        l2_finished = true;
                    }
                } else if (l2->next == nullptr) {
                    l2_finished = true;
                }
                l1 = l1->next;
                l2 = l2->next;
            }

        }
        if (carry > 0) {;
            l1->next = new ListNode(carry);
        }
        return ret;
    }
};

// Solution End --------------
#ifdef LOCAL_RUN

ListNode *toListNode(vector<int> &vec) {
    auto it = vec.begin();
    auto ptr = new ListNode(*it);
    ListNode *ret = ptr;

    for (++it; it != vec.end(); it++) {
        auto tem = new ListNode(*it);
        ptr->next = tem;
        ptr = ptr->next;
    }
    return ret;
}

bool areIdentical(ListNode *a, ListNode *b) {
    while (a != nullptr && b != nullptr) {
        if (a->val != b->val)
            return false;

        a = a->next;
        b = b->next;
    }
    return (a == nullptr && b == nullptr);
}

void printLinkedList(ListNode *l) {
    while(l != nullptr) {
        cout << l->val << " -> ";
        l = l->next;
    }
    cout << "END" << endl;
}

int main() {
    Solution sol;
    vector<vector<vector<int>>> inputs = {
            {{9, 9, 9, 9, 9, 9, 9}, {9, 9, 9, 9}},
            {{0},                   {0}}
    };
    vector<vector<int>> expecteds = {
            {8, 9, 9, 9, 0, 0, 0, 1},
            {0}
    };
    for (int i = 0; i < inputs.size(); i++) {
        ListNode *l1 = toListNode(inputs[i][0]);
        ListNode *l2 = toListNode(inputs[i][1]);
        printLinkedList(l1);
        printLinkedList(l2);
        ListNode *expected = toListNode(expecteds[i]);
        ListNode *output = sol.addTwoNumbers(l1, l2);
        printLinkedList(expected);
        printLinkedList(output);

        if (areIdentical(expected, output)) {
            std::cout << i << " Matched" << endl;
        } else {
            std::cout << i << " Not Matched" << endl;
        }
    }

    return 0;
}

#endif