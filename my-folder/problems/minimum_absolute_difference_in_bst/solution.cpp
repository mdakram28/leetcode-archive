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
    int prev = -10e6;
    int ans = 10e6;
    void travel(TreeNode* node) {
        if (node == nullptr) return;

        travel(node->left);

        ans = min(ans, node->val - prev);
        prev = node->val;

        travel(node->right);
    }

    int getMinimumDifference(TreeNode* root) {
        travel(root);
        return ans;
    }
};