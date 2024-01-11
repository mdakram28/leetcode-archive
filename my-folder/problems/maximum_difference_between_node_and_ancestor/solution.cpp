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
    std::pair<int, int> dfs(TreeNode* node, int &ans)
    {
        int a = node->val, b = node->val;
        
        if (node->left)
        {
            auto [x, y] = dfs(node->left, ans);
            ans = std::max(ans, std::max(
                std::abs(node->val - x),
                std::abs(node->val - y)
            ));

            a = std::min(a, x);
            b = std::max(b, y);
        }
        if (node->right)
        {
            auto [x, y] = dfs(node->right, ans);
            ans = std::max(ans, std::max(
                std::abs(node->val - x),
                std::abs(node->val - y)
            ));

            a = std::min(a, x);
            b = std::max(b, y);
        }

        std::cout << "a = " << a << ", b = " << b << endl;

        return {a, b};
    }
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }
};