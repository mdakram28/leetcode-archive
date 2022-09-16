class Solution {
public:
    int maximumScore(vector<int> &nums, vector<int> &multipliers) {
        auto nSize = nums.size();
        auto mSize = multipliers.size();
        vector<int> dp(nSize);

        int len = nSize - mSize;

        for (int mi = mSize-1; mi>=0; mi--) {
            int iLimit = nSize - len;
            if (len == 0) {
                for (int i = 0; i < iLimit; i++) {
                    dp[i] = multipliers[mi] * nums[i] + dp[i];
                }
            } else {
                for (int i = 0; i < iLimit; i++) {
                    dp[i] = max(multipliers[mi] * nums[i] + dp[i + 1], multipliers[mi] * nums[i + len] + dp[i]);
                }
            }
            len++;
        }

        return dp[0];
    }
};