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

using level_t = vector<TreeNode *>;
class Solution {
public:
    bool should_be_null(level_t::iterator it, level_t::iterator end) {
        for (;it != end; ++it) {
            if (*it != nullptr) return false;
        }
        return true;
    }

    bool isCompleteTree(TreeNode* root) {
        level_t *level = new level_t();
        level_t *next_level = new level_t();

        level->push_back(root);

        while (level->size() > 0) {
            next_level->clear();
            for (auto it = level->begin(); it != level->end(); ++it) {
                if (*it != nullptr) {
                    next_level->push_back((*it)->left);
                    next_level->push_back((*it)->right);
                } else {
                    return should_be_null(it, level->end()) && should_be_null(next_level->begin(), next_level->end());
                }
            }

            level_t *temp = next_level;
            next_level = level;
            level = temp;
        }
        return true;
    }
};