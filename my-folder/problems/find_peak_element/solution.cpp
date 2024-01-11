class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size()-1;

        while (l<r)
        {
            // printf("l=%d, r=%d\n", l, r);
            int m = l + (r-l)/2;
            long mid = nums[m];
            long left = m > 0 ? nums[m-1] : mid-1;
            long right = m < nums.size()-1 ? nums[m+1] : mid+1;
            if (mid > left && mid > right) 
                return m;
            else if (left < mid && mid < right)
                l = m+1;
            else
                r = m;
        }
        return l;
    }
};