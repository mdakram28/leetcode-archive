class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        vector<pair<int, int>> pos(m*n+1);
        for (int r=0; r<m; r++) {
            for (int c=0; c<n; c++) {
                pos[mat[r][c]] = make_pair(r, c);
            }
        }
        
        vector<int> remRow(m, n);
        vector<int> remCol(n, m);

        for(int i=0; i<arr.size(); i++) {
            auto p = pos[arr[i]];
            remRow[p.first]--;
            remCol[p.second]--;
            if (remRow[p.first] == 0 || remCol[p.second] == 0) {
                return i;
            }
        }
        return arr.size();
    }
};