class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if (nums.size()==0) return ans;
        int start = nums[0];
        int i=1;
        for(; i<nums.size(); i++) {
            if(((long)nums[i])-nums[i-1] != 1) {
                if(start == nums[i-1]) {
                    ans.push_back(to_string(start));
                } else {
                    ans.push_back(to_string(start) + "->" + to_string(nums[i-1]));
                }
                start = nums[i];
            }
        }
        
        if(start == nums[i-1]) {
            ans.push_back(to_string(start));
        } else {
            ans.push_back(to_string(start) + "->" + to_string(nums[i-1]));
        }

        return ans;
    }
};