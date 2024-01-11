class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int l=0, r=0;
        const int n = nums.size();
        int z = 0;
        int ans = 0;
        while (r < n) {
            if (nums[r++] == 0) {
                z++;
            }
            while (z > 1) {
                if(nums[l] == 0) {
                    z--;
                }
                l++;
            }
            ans = std::max(ans, r-l-1);
        }
        return ans;
    }
};