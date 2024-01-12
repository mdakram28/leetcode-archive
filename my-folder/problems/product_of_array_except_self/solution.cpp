class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int n = nums.size();
        std::vector<int> ret(n);

        int prod = 1;
        for(int i=n-1; i>=0; i--) {
            ret[i] = prod;
            prod *= nums[i];
        }

        prod = 1;
        for(int i=0; i<n; i++) {
            ret[i] *= prod;
            prod *= nums[i];
        }

        return ret;
    }
};