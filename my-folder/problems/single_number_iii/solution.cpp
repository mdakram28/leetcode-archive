class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        uint64_t x = 0;
        for (int num: nums)
        {
            x ^= num;
        }
        uint64_t diffbit = x^(x&(x-1));
        uint64_t x0=0, x1=0;
        for (int num: nums)
        {
            if (num&diffbit)
            {
                x1 ^= num;
            } else {
                x0 ^= num;
            }
        }
        return {(int)x0, (int)x1};
    }
};