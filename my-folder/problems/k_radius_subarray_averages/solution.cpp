class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n=nums.size();
        vector<int> ans(n, -1);

        int w = 2*k+1;
        if (w > n) return ans;

        long total = 0;
        int i = 0;

        while (i<w) {
            total += nums[i];
            i++;
        }
        // cout << total << endl;
        ans[i-k-1] = total/w;

        while(i<n) {
            total += nums[i] - nums[i-w];
            ans[i-k] = total/w;
            i++;
        }
        return ans;
    }
};