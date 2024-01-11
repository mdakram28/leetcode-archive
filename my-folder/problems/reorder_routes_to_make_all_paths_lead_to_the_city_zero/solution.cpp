class Solution {
public:
    int dfs(int at, std::vector<std::vector<std::pair<int, int>>> &g, int p) {
        int total = 0;
        // cout << "at = " << at << endl;
        for(auto [to, cost]: g[at]) {
            if (to == p) continue;
            // cout << "to = " << to << ", cost = " << cost << endl;
            total += dfs(to, g, at);
            total += cost;
        }
        return total;
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        
        for(int i=0; i<connections.size(); i++) {
            int from = connections[i][0];
            int to = connections[i][1];
            g[from].push_back({to, 1});
            g[to].push_back({from, 0});
        }
        return dfs(0, g, -1);
    }
};