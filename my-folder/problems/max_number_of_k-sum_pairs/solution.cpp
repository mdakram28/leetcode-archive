class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        const int n = nums.size();
        int count = 0;
        int l=0, r=n-1;
        while (l < r) {
            const int total = nums[l] + nums[r];
            if (total == k) {
                count++;
                l++;r--;
            } else if (total < k) {
                l++;
            } else {
                r--;
            }
        }
        return count;
    }
};