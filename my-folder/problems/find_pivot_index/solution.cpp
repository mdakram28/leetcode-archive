class Solution {
public:
    int pivotIndex(vector<int> &nums) {
//        auto size = nums.size();
        long sum_total = accumulate(nums.begin(), nums.end(), 0);
        long sum_left = 0;
        for (int i = 0; i < nums.size(); i++) {
            if(!(2*sum_left - sum_total + nums[i])) {
                return i;
            }
            sum_left += nums[i];
        }
        return -1;
    }
};