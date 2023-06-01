class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        int minVal = INT_MAX;
        vector<pair<int, int>> st;

        for(int k = 0; k<n; k++) {
            // printf("%d: %d \n", k, nums[k]);
            // for(auto [i, j]: st) {
            //     printf("(%d, %d), ", i, j);
            // }
            // cout << endl;

            if (st.size() > 0) {
                auto ind = lower_bound(st.begin(), st.end(), make_pair(nums[k], INT_MAX), greater<pair<int, int>>())-st.begin()-1;
                // printf("ind=%d\n", ind);
                if (ind >= 0) {
                    auto [j, i] = st[ind];
                    if (i < nums[k]) return true;
                }
            }
            
            while (st.size() > 0 && st[st.size()-1].first<=nums[k]) {
                st.pop_back();
            }
            st.push_back(make_pair(nums[k], minVal));

            if (nums[k] < minVal) minVal = nums[k];
        }

        return false;
    }
};