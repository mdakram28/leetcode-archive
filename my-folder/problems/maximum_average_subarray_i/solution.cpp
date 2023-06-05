class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int i=0;
        int total = 0;
        while(i<k) {
            total += nums[i];
            i++;
        }
        int ans = total;
        while(i<n) {
            total += nums[i]-nums[i-k];
            if (total > ans) {
                ans = total;
            }
            i++;
        }
        return ((double)ans)/k;
    }
};