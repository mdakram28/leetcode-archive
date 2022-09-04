class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        auto size = lists.size();
        int nullCounter = 0;
        if (size == 0) {
            return nullptr;
        }
        int minIndex1 = 0;
        int minValue1 = 100000;
        for (int i = 0; i < size; i++) {
            if (lists[i] == nullptr) {
                nullCounter++;
            } else if (lists[i]->val < minValue1) {
                minIndex1 = i;
                minValue1 = lists[i]->val;
            }
        }
        if (nullCounter == size) {
            return nullptr;
        } else if (nullCounter == size - 1) {
            for (int i = 0; i < size; i++) {
                if (lists[i] != nullptr) return lists[i];
            }
        }
        int minIndex2 = 0;
        int minValue2 = 100000;
        for (int i = 0; i < size; i++) {
            if (lists[i] != nullptr && i != minIndex1 && lists[i]->val <= minValue2) {
                minIndex2 = i;
                minValue2 = lists[i]->val;
            }
        }

        ListNode *mergedHead, *mergedTail;
        mergedHead = lists[minIndex1];
        mergedTail = getNodeUpto(mergedHead, minValue2);
//        cout << "minIndex1=" << minIndex1 << ", minIndex2=" << minIndex2 << endl;
//        cout << "MergedHead = "; printLL(mergedHead);

        lists[minIndex1] = mergedTail->next;
        if (lists[minIndex1] == nullptr) {
            nullCounter++;
        }
        mergedTail->next = nullptr;


        while (nullCounter < (size - 1)) {
            minIndex1 = minIndex2;
//            minValue1 = minValue2;
            minValue2 = 100000;
            for (int i = 0; i < size; i++) {
                if (lists[i] != nullptr && i != minIndex1 && lists[i]->val <= minValue2) {
                    minIndex2 = i;
                    minValue2 = lists[i]->val;
                }
            }

            ListNode *minList = lists[minIndex1];
            mergedTail->next = minList;
            mergedTail = getNodeUpto(minList, minValue2);
            lists[minIndex1] = mergedTail->next;
            if (lists[minIndex1] == nullptr) {
                nullCounter++;
            }
            mergedTail->next = nullptr;
//            cout << "minIndex1=" << minIndex1 << ", minIndex2=" << minIndex2 << endl;
//            cout << "MergedHead = "; printLL(mergedHead);
        }

        mergedTail->next = lists[minIndex2];
        return mergedHead;
    }

    static ListNode *getNodeUpto(ListNode *node, int val) {
        ListNode *lastNode = node;
        node = node->next;
        while (node != nullptr) {
            if (node->val > val) {
                return lastNode;
            }
            lastNode = node;
            node = node->next;
        }
        return lastNode;
    }
};