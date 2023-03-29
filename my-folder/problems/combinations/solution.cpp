class Solution {
    vector<vector<int>> ret;
    vector<int> prefix;
    vector<int> nums;
    int n, k;
public:
    void add_all_comb(int i) {
        if (prefix.size() >= k) {
            ret.push_back(prefix);
            return;
        }
        int last = (n-k+1) + prefix.size();
        for(;i<=n;i++) {
            prefix.push_back(i);
            add_all_comb(i+1);
            prefix.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        this->n = n;
        this->k = k;

        for(int i=nums.size()+1; i<=n; i++) {
            nums.push_back(i);
        }

        ret.clear();
        prefix.clear();
        add_all_comb(1);

        return ret;
    }
};