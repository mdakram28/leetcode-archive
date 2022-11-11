class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int top = 0;
        int l = nums.size();
        for(int i=1;i<l;i++) {
            if (nums[i] != nums[top]) {
                nums[++top] = nums[i];
            }
        }
        return top+1;
    }
};