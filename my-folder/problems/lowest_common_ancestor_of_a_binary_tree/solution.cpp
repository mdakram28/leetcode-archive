/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int find(TreeNode* at, TreeNode* p, TreeNode* q, TreeNode* &ans) {
        if (at == nullptr) return 0;
        int val = at == p ? 1 : (at == q ? 2 : 0);
        val |= find(at->left, p, q, ans);
        if (val == 3) {
            ans = at;
            return 0;
        }
        if (ans) return 0;
        val |= find(at->right, p, q, ans);
        if (val == 3) {
            ans = at;
            return 0;
        }

        return val;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* ans = nullptr;
        find(root, p, q, ans);
        return ans;
    }
};