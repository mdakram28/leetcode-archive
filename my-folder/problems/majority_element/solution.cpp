class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int me = nums[0];
        int c = 0;
        for(int n: nums)
        {
            if (n == me)
                c++;
            else
                c--;

            if (c == 0)
            {
                me = n;
                c = 1;
            }
        }

        return me;
    }
};