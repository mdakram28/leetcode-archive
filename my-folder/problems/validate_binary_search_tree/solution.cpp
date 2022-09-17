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
    bool isValidBST(TreeNode* root) {
        return isValidNode(root, INT_MIN, INT_MAX);
    }
    
    bool isValidNode(TreeNode* node, long l, long u) {
        if (!node) return true;
        if (node->val < l || node->val > u) return false;
        
        return isValidNode(node->left, l, ((long)node->val)-1) && isValidNode(node->right, ((long)node->val)+1, u);
    }
};