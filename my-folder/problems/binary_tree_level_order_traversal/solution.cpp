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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode *> q;
        vector<vector<int>> ret;
        vector<TreeNode *> thisLevel = {root};
        if(!root) {
            return ret;
        }
        
        while(thisLevel.size() > 0) {
            vector<TreeNode *> nextLevel;
            vector<int> thisLevelValues;
            for(auto node: thisLevel) {
                thisLevelValues.push_back(node->val);
                if(node->left) {
                    nextLevel.push_back(node->left);
                }
                if(node->right) {
                    nextLevel.push_back(node->right);
                }
            }
            ret.push_back(thisLevelValues);
            thisLevel = nextLevel;
        }
        return ret;
    }
};