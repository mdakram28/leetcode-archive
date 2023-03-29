class Solution {
    vector<vector<int>> ret;
    vector<int> nums;
    vector<int> prefix;
    vector<int> freq;
public:
    void add_till_empty() {
        if (prefix.size() == nums.size()) {
            ret.push_back(prefix);
            return;
        }
        for (auto it = nums.begin(); it != nums.end();) {
            auto num = *it;
            if (freq[num+10] == 0) {
                ++it;
                continue;
            }
            // printf("Reading freq[%d]\n", num);
            freq[num+10]--;
            prefix.push_back(num);
            add_till_empty();
            prefix.pop_back();
            freq[num+10]++;
            while (it!=nums.end() && *it == num) {
                ++it;
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        this->nums = nums;

        freq.resize(25);
        fill(freq.begin(), freq.end(), 0);
        ret.clear();
        for (auto num : nums) {
            freq[num+10]++;
        }

        prefix.clear();
        add_till_empty();
        return ret;
    }
};