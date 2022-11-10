class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        set<int> last;
        int l = nums.size();
        
        int lower_i = 0;
        for(int i=0;i<l;i++) {
            int lb = nums[i]-valueDiff;
            int ub = nums[i]+valueDiff;
            auto slb = last.lower_bound(lb);
            // auto sub = last.upper_bound(ub);
            // printf("i=%d, Lower Bound (%d) = %d, Upper Bound (%d) = %d \n", 
            //       i, lb, *slb, ub, *sub);
            if((slb != last.end() && *slb <= ub)) {
                return true;
            }
            
            last.insert(nums[i]);
            if(last.size() > indexDiff) {
                last.erase(nums[i-indexDiff]);
            }
        }
        return false;
    }
};