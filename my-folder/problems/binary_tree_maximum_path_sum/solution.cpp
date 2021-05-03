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

struct ret {
    int p;
    int t;
};
class Solution {
    int min_val = INT_MAX;
    
    void get_min_val(TreeNode* n) {
        if(n == NULL) return;
        get_min_val(n->left);
        get_min_val(n->right);
        
        min_val = min({min_val, n->val, 0});
    }
    
    ret traverse(TreeNode *n, int t) {
        if(n == NULL) return {min_val-1,min_val-1};
        
        ret l = traverse(n->left, t+1);
        ret r = traverse(n->right, t+1);
        
        // for(int i=0;i<t;i++) cout << "  ";
        // cout << n->val << " : ";
        // cout << l.p << "," << l.t << "    ";
        // cout << r.p << "," << r.t << endl;
        
        int val = n->val;
        return {
            max({l.p,r.p, 0}) + val,
            max({l.p+val, r.p+val, l.p+r.p+val, l.t, r.t, val})
        };
    }
public:
    int maxPathSum(TreeNode* root) {
        get_min_val(root);
        ret ans = traverse(root,1);
        return max(ans.p, ans.t);
    }
};