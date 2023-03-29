class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        if (grid[0][0] == 1) return 0;
        
        int m = grid.size(), n = grid[0].size();
        int r = 0, c = 0;
        while (c < n && grid[r][c] != 1) {
            grid[r][c] = 1;
            c++;
        }
        while (c < n) {
            grid[r][c] = 0;
            c++;
        }
        c=0;
        r=1;
        while (r < m && grid[r][c] != 1) {
            grid[r][c] = 1;
            r++;
        }
        while (r < m) {
            grid[r][c] = 0;
            r++;
        }

        for (r=1; r<m; r++) {
            for (c=1; c<n; c++) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 0;
                } else {
                    grid[r][c] = grid[r-1][c] + grid[r][c-1];
                }
            }
        }
        return grid[m-1][n-1];
    }
};