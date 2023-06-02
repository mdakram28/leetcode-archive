class Solution {
public:
    int dfs(int at, vector<int> &visited, vector<vector<int>> &g) {
        if (visited[at]) return 0;
        visited[at] = 1;

        int total = 1;
        for (int to: g[at]) {
            total += dfs(to, visited, g);
        }
        return total;
    }
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector<vector<int>> g(n);

        for(int i=0; i<n; i++) {
            long x1 = bombs[i][0];
            long y1 = bombs[i][1];
            long r1 = long(bombs[i][2])*long(bombs[i][2]);
            for(int j=0; j<n; j++) {
                if (i==j) continue;
                long x2 = bombs[j][0];
                long y2 = bombs[j][1];

                long d = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
                if (d <= r1) {
                    g[i].push_back(j);
                }
            }
        }

        int ans = 0;
        for(int i=0; i<n; i++) {
            vector<int> visited(n);
            ans = max(ans, dfs(i, visited, g));
        }

        return ans;

    }
};