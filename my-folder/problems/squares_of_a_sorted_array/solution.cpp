class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int size = nums.size();
        vector<int> ret (size, 0);
        
        int right = 0;
        while(right < size && nums[right] < 0) {
            right++;
        }
        int left = right-1;
        int i = 0;
        
        while(left >= 0 && right < size) {
            if ((-nums[left]) < nums[right] ) {
                ret[i++] = nums[left]*nums[left];
                left--;
            } else {
                ret[i++] = nums[right]*nums[right];
                right++;
            }
        }
        
        while(left >= 0) {
            ret[i++] = nums[left]*nums[left];
            left--;
        }
        
        while(right < size) {
            ret[i++] = nums[right]*nums[right];
            right++;
        }
            
        return ret;
    }
};