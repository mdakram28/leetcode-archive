class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> orig(nums.size());
        copy(nums.begin(), nums.end(), orig.begin());
        
        sort(nums.begin(), nums.end());
        
        int li = 0;
        int ri = nums.size()-1;
        
        while(li < ri) {
            int sum = nums[li] + nums[ri];
            if(sum == target) {
                int oli = find(orig.begin(), orig.end(), nums[li]) - orig.begin();
                orig[oli] = nums[ri] - 1;
                return {
                    oli,
                    find(orig.begin(), orig.end(), nums[ri]) - orig.begin()
                };
            } else if(sum < target) {
                li++;
            } else {
                ri--;
            }
        }
        return {};
    }
};