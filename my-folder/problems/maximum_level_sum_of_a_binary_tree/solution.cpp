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
    int maxLevelSum(TreeNode* root) {
        std::queue<TreeNode*> q; 
        q.push(root);
        int n;
        long maxSum = INT_MIN;
        int maxLevel = 1;
        int level=0;
        while((n = q.size()) > 0) {
            level++;
            long sum = 0;
            for(int i=0; i<n; i++) {
                auto at = q.front();
                if (at->left) q.push(at->left);
                if (at->right) q.push(at->right);
                q.pop();
                sum += at->val;
            }
            if (sum > maxSum) {
                maxLevel = level;
                maxSum = sum;
            }
        }
        return maxLevel;
    }
};