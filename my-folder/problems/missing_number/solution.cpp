class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        return ((n*(n+1))/2) - reduce(nums.begin(), nums.end());
    }
};