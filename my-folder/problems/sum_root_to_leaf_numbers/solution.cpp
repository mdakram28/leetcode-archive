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
    int total;
public:
    void add_all(TreeNode* node, int pref) {
        if (node->left == nullptr && node->right == nullptr) {
            total += pref;
        } else {
            if (node->left != nullptr) {
                add_all(node->left, pref*10 + node->left->val);
            }
            if (node->right != nullptr) {
                add_all(node->right, pref*10 + node->right->val);
            }
        }
    }

    int sumNumbers(TreeNode* root) {
        if (root == nullptr) return 0;
        add_all(root, root->val);
        return total;
    }
};