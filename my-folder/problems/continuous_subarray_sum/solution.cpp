class Solution {
public:
    bool checkSubarraySum(vector<int> &nums, int k) {
        map<int, int> pos;
        auto size = nums.size();
        pos[0] = -1;
        int rem = 0;
        auto end = pos.end();

        for (int i = 0; i < size; i++) {
            rem = (rem + nums[i]) % k;
//            cout << "rem=" << rem << endl;
            if (pos.find(rem) != end) {
                if (pos[rem] <= i-2) {
                    return true;
                }
            } else {
                pos[rem] = i;
            }
        }
        return false;
    }
};