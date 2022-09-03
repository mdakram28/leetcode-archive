class Solution {
public:
    vector<int> runningSum(vector<int> &nums) {
        size_t size = nums.size();
        int sum = 0;
//        vector<int> ret(size);
        for (int i = 0; i < size; i++) {
            sum += nums[i];
            nums[i] = sum;
        }
        return nums;
    }
};