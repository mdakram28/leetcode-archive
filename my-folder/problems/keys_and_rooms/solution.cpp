class Solution {
public:

    void dfs(int at, vector<vector<int>>& g, std::vector<bool> &seen) {
        if (seen[at]) return;
        seen[at] = true;
        for(auto to: g[at]) {
            dfs(to, g, seen);
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        std::vector<bool> seen(n);

        dfs(0, rooms, seen);

        int ans = 0;
        for(bool s: seen) {
            if (s) ans++;
        }
        return ans == n;
    }
};