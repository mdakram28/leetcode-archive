class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int i=0;
        int n = nums.size();
        while(i<n && nums[i]==1) i++;
        if (i==n) return n-1;
        i++;

        int start = 0;
        int ans = i;
        
        while (i<n) {
            if (nums[i] == 0) {
                ans = max(ans, i-start);
                
                while(nums[start]==1) {
                    start++;
                }
                start++;
            }
            i++;
        }
        // printf("[%d:%d]\n", start, i);
        ans = max(ans, i-start);
        return ans-1;
    }
};