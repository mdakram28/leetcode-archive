
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        std::array<std::pair<int, int>, 4> diff ({
            {-1, 0}, {1, 0}, {0, -1}, {0, 1}
        });
        std::queue<std::pair<int, int>> q;
        int m = grid.size(), n=grid[0].size();
        int t = 0;
        int numFresh = 0;
        
        // Populate q with rotten
        for(int r=0; r<m; r++) {
            for(int c=0; c<n; c++) {
                if (grid[r][c] == 2) {
                    q.push({r, c});
                } else if (grid[r][c] == 1) {
                    numFresh++;
                }
            }
        }
        
        while(q.size() > 0) {
            int s = q.size();
            for(int i=0; i<s; i++) {
                auto [r, c] = q.front();
                // cout << r << ", " << c << endl;
                q.pop();
                for(auto [dr, dc] : diff) {
                    // cout << dr << ", " << dc << " | ";
                    int nr = r+dr, nc = c+dc;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        q.push({nr, nc});
                        grid[nr][nc] = 2;
                        numFresh--;
                    }
                }
            }
            t++;
        }

        // cout << t << endl;

        return numFresh == 0 ? std::max(t-1, 0) : -1;
    }
};