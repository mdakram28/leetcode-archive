class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        int j = 0;
        for (int i=0; i<nums.size(); i++)
        {
            if (nums[i]%2 == 0)
            {
                nums[j++] = nums[i];
            }
        }
        if (j == 0)
        {
            return -1;
        }
        nums.resize(j);
        
        sort(nums.begin(), nums.end());

        int prev = nums[0];
        int count = 0;
        j = 0;

        int me = nums[0];
        int mecount = 1;

        for(int i=0; i<nums.size(); i++)
        {
            if (nums[i] == prev)
            {
                count++;
                continue;
            }

            if (count > mecount)
            {
                mecount = count;
                me = prev;
            } else if (count == mecount && prev < me)
            {
                me = prev;
            }

            prev = nums[i];
            count = 1;
        }
        nums[j++] = count;

        if (count > mecount)
        {
            mecount = count;
            me = prev;
        } else if (count == mecount && prev < me)
        {
            me = prev;
        }

        return me;
    }
};