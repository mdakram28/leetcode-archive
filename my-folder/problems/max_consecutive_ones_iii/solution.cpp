class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        const int n = nums.size();
        int l=0, r=0, z=0;
        int ans = 0;
        while (r < n) {
            if (nums[r++] == 0) z++;
            
            while (z > k) {
                if (nums[l] == 0) z--;
                l++;
            }

            if (r-l > ans) {
                ans = r-l;
            }
        }
        return ans;
    }
};