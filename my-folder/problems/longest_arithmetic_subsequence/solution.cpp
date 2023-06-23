class Solution {
int max_len[1000][1001];
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for(int i=0; i<n; i++) {
            for (int j=0; j<i; j++) {
                int d = nums[i]-nums[j]+500;
                int l = max_len[j][d]+1;
                max_len[i][d] = l;
                if (l > ans) {
                    ans = l;
                }
            }
        }
        return ans+1;
    }
};