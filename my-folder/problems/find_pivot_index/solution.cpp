class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        long right = std::reduce(nums.begin(), nums.end());
        long left = 0;
        for(int i=0; i<nums.size(); i++) {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }
        return -1;
    }
};