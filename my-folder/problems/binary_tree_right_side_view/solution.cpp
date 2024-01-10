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
    void dfs(TreeNode* node, vector<int> &ret, int d=0) {
        if (node == nullptr) return;
        if (ret.size() <= d) {
            ret.resize(d+1);
        }
        ret[d] = node->val;
        dfs(node->left, ret, d+1);
        dfs(node->right, ret, d+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        dfs(root, ret);
        return ret;
    }
};