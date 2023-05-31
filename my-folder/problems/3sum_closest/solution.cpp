class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = nums[0] + nums[1] + nums[2];
        for(int i=0; i<n; i++) {
            int t = target-nums[i];
            int j=i+1, k = n-1;
            while (j<k) {
                if (abs(target-nums[i]-nums[j]-nums[k]) < abs(target-ans)) {
                    ans = nums[i]+nums[j]+nums[k];
                }
                if (nums[j]+nums[k] < t) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return ans;
    }
};