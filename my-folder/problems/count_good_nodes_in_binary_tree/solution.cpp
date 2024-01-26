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
    int dfs(TreeNode* node, int maxVal) {
        if (node == nullptr) return 0;
        int total = 0;
        if (node->val >= maxVal) {
            total++;
        }
        maxVal = std::max(maxVal, node->val);
        total += dfs(node->left, maxVal);
        total += dfs(node->right, maxVal);
        return total;
    }
    int goodNodes(TreeNode* root) {
        return dfs(root, INT_MIN);
    }
};