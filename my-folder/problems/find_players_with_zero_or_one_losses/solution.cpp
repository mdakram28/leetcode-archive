class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        std::map<int, int> lost;
        for (auto& v : matches) {
            int w = v[0], l = v[1];
            lost[l]++;
            lost[w];
        }
        std::vector<std::vector<int>> ans(2);
        for (auto& [pl, c] : lost) {
            if (c == 0)
                ans[0].push_back(pl);
            else if (c == 1)
                ans[1].push_back(pl);
        }
        return ans;
    }
};