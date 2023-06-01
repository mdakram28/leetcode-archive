#define T tuple<int, int, int>

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid[0][0] == 1) return -1;

        int n = grid.size(), d, r, c;
        priority_queue<T, vector<T>, greater<T>> q;
        vector<vector<int>> dist(n, vector(n, INT_MAX));

        q.push(make_tuple(1, 0, 0));
        dist[0][0] = 1;

        while(q.size() > 0) {
            tie (d, r, c) = q.top();
            q.pop();
            d++;

            for(int dr=-1; dr<=1; dr++) {
                int nr=r+dr;
                if (nr<0 || nr>=n) continue;
                for(int dc=-1; dc<=1; dc++) {
                    int nc=c+dc;
                    if (nc<0 || nc>=n) continue;
                    if (grid[nr][nc] == 0 && d < dist[nr][nc]) {
                        dist[nr][nc] = d;
                        q.push(make_tuple(d, nr, nc));
                    }
                }
            }
        }

        // for(int r=0; r<n; r++) {
        //     for(int c=0; c<n; c++) {
        //         cout << dist[r][c] << ", ";
        //     }
        //     cout << endl;
        // }

        return dist[n-1][n-1] != INT_MAX ? dist[n-1][n-1] : -1;
    }
};