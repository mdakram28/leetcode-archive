class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        long long sum = std::reduce(nums.begin(), nums.begin() + k);
        long long maxSum = sum;

        for(int i=k; i<nums.size(); i++) {
            sum += nums[i]-nums[i-k];
            maxSum = std::max(sum, maxSum);
        }

        return maxSum/(double)k;
    }
};