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
    int dfs(TreeNode* node, long prevSum, long targetSum, std::unordered_map<long, long> &prevCount) {
        if (node == nullptr) return 0;
        prevSum += node->val;
        long rem = prevSum-targetSum;
        int total = prevCount[rem];

        prevCount[prevSum]++;
        total += dfs(node->left, prevSum, targetSum, prevCount);
        total += dfs(node->right, prevSum, targetSum, prevCount);
        prevCount[prevSum]--;

        return total;
    }
    int pathSum(TreeNode* root, int targetSum) {
        std::unordered_map<long, long> prevCount;
        prevCount[0] = 1;
        return dfs(root, 0, targetSum, prevCount);
    }
};