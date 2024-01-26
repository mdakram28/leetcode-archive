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
public:
    TreeNode* leftMost(TreeNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    TreeNode* remove(TreeNode* node) {
        // cout << "Removing" << node->val << endl;
        if (node->left == nullptr) {
            return node->right;
        } else if (node->right == nullptr) {
            return node->left;
        }
        TreeNode* succ = leftMost(node->right);
        node->val = succ->val;
        node->right = deleteNode(node->right, succ->val);
        return node;
    }

    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) return nullptr;
        if (root->val == key) {
            return remove(root);
        } else if (key < root->val) {
            root->left = deleteNode(root->left, key);
            return root;
        } else {
            root->right = deleteNode(root->right, key);
            return root;
        }
    }
};