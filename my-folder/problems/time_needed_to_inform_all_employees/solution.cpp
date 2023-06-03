class Solution {
    int dfs(int at, vector<vector<int>>& g, vector<int>& informTime) {
        if (g[at].size() == 0) return 0;
        int ans = 0;
        for(int to: g[at]) {
            ans = max(ans, dfs(to, g, informTime));
        }
        return ans+informTime[at];
    }
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> g(n);

        for(int i=0; i<headID; i++) {
            g[manager[i]].push_back(i);
        }
        for(int i=headID+1; i<n; i++) {
            g[manager[i]].push_back(i);
        }

        return dfs(headID, g, informTime);
    }
};