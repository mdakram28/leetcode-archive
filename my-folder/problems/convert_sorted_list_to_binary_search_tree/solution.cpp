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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int length = 0;
    int maxDepth = 0;
public:
    ListNode* addTreeNodesLeft(TreeNode* root, ListNode* head, int d) {
        if (d > maxDepth || head == nullptr) {
            return head;
        }
        TreeNode *node = new TreeNode();
        root->left = node;
        head = addTreeNodesLeft(node, head, d+1);
        printf("Adding to left : %d\n", head->val);
        node->val = head->val;
        head = head->next;
        if (head == nullptr) return head;
        head = addTreeNodesRight(node, head, d+1);
        return head;
    }
    ListNode* addTreeNodesRight(TreeNode* root, ListNode* head, int d) {
        if (d > maxDepth || head == nullptr) {
            return head;
        }
        TreeNode *node = new TreeNode();
        root->right = node;
        if (head->next != nullptr) {
            head = addTreeNodesLeft(node, head, d+1);
        }
        printf("Adding to right : %d\n", head->val);
        node->val = head->val;
        head = head->next;
        if (head == nullptr) return head;
        head = addTreeNodesRight(node, head, d+1);
        return head;
    }
    TreeNode* sortedListToBST_old(ListNode* head) {
        if (head == nullptr) return nullptr;

        ListNode *node = head;
        while (node != nullptr) {
            node = node->next;
            length++;
        }
        
        int totalNodes = 1;
        int nodesInLevel = 1;
        while (totalNodes < length) {
            maxDepth += 1;
            nodesInLevel *= 2;
            totalNodes += nodesInLevel;
        }
        
        TreeNode *root = new TreeNode();
        head = addTreeNodesLeft(root, head, 1);
        root->val = head->val;
        head = head->next;
        if (head == nullptr) return root;
        addTreeNodesRight(root, head, 1);
        return root;
    }

    ListNode* setValues(TreeNode* node, ListNode* head) {
        if (node == nullptr) return head;
        head = setValues(node->left, head);
        node->val = head->val;
        head = head->next;
        head = setValues(node->right, head);
        return head;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr) return nullptr;
        ListNode* node = head;
        vector<TreeNode *> treeNodes;

        int i = 0;
        TreeNode* root = new TreeNode();
        treeNodes.push_back(root);
        node = node->next;

        while (node != nullptr) {
            TreeNode *treeNode = treeNodes[i++];
            treeNode->left = new TreeNode();
            treeNodes.push_back(treeNode->left);
            node = node->next;

            if (node == nullptr) break;
            treeNode->right = new TreeNode();
            treeNodes.push_back(treeNode->right);
            node = node->next;
        }


        setValues(root, head);
        return root;
    }
};