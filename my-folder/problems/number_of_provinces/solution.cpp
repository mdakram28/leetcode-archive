class Solution {
public:
    void visit(int at, vector<vector<int>>& isConnected, vector<bool> &visited) {
        visited[at] = true;
        for(int to=0; to<isConnected[at].size(); to++) {
            if (isConnected[at][to] && !visited[to]) {
                visit(to, isConnected, visited);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected[0].size();
        vector<bool> visited(n);
        int ans = 0;
        for (int at=0; at<n; at++) {
            if (!visited[at]) {
                visit(at, isConnected, visited);
                ans++;
            }
        }
        return ans;
    }
};