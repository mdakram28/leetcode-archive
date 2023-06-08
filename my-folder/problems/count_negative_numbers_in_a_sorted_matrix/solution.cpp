class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int c=n;
        int total=0;
        for(int r=0; r<m; r++) {
            while(c && grid[r][c-1]<0) {
                c--;
            }
            total += c;
        }
        return m*n - total;
    }
};