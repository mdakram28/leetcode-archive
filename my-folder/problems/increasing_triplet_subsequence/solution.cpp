class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> maxRight(n);
        
        int currMax = nums[n-1];
        for(int i=n-2; i>=0; i--) {
            maxRight[i] = currMax;
            currMax = std::max(currMax, nums[i]);
        }

        int currMin = nums[0];
        for(int i=1; i<n-1; i++) {
            if (currMin < nums[i] && nums[i] < maxRight[i]) return true;
            currMin = std::min(currMin, nums[i]);
        }

        return false;
    }
};