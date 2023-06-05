class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> vals;
        int t = 0;
        for(int num: nums) {
            if (vals[k-num]) {
                vals[k-num]--;
                t++;
            } else {
                vals[num]++;
            }
        }
        return t;
    }
};