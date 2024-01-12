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
    std::pair<int, int> dfs(TreeNode* node, int &ans) {
        if (!node) return {0, 0};
        auto l = dfs(node->left, ans);
        auto r = dfs(node->right, ans);
        std::pair<int, int> ret = {
            node->left ? 1 + l.second : 0,
            node->right ? 1 + r.first : 0
        };
        ans = std::max(ans, std::max(ret.first, ret.second));
        return ret;
    }
    int longestZigZag(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }
};