#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define pbds                                               \
    tree<pair<int, int>, null_type, less<pair<int, int> >, \
         rb_tree_tag, tree_order_statistics_node_update>
using namespace __gnu_pbds;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        pbds s;
        int len = nums.size();
        // s.reserve(len);
        s.insert({nums[len-1], len-1});
        nums[len-1] = 0;
        for(int i=len-2;i>=0;i--) {
            int num = nums[i];
            nums[i] = s.order_of_key({num, i});
            s.insert({num, i});
        }
        return nums;
    }
};