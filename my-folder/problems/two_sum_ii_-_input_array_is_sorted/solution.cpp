class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int size = nums.size();
        int l = 0;
        int r = size-1;
        vector<int> ret = {0,0};
        while(l<r) {
            int total = nums[l] + nums[r];
            if (total == target) {
                ret[0] = l+1;
                ret[1] = r+1;
                return ret;
            } else if (total < target) {
                l++;
            } else {
                r--;
            }
        }
        return ret;
    }
};