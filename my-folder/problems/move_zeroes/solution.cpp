class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int size = nums.size();
        int i = 0;
        while(i<size && nums[i]) {
            i++;
        }
        
        int swapPos = i;
        i++;
        while(i<size) {
            if(nums[i]) {
                nums[swapPos] = nums[i];
                nums[i] = 0;
                swapPos++;
            }
            i++;
        }
        
    }
};