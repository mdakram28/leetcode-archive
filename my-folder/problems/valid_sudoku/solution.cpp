class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rowMap(9, vector<int>(9));
        vector<vector<int>> colMap(9, vector<int>(9));
        vector<vector<int>> boxMap(9, vector<int>(9));
        
        for(int r=0;r<9;r++) {
            for(int c=0;c<9;c++) {
                if (board[r][c] == '.') continue;
                int v = board[r][c] - '1';
                if (rowMap[r][v] || colMap[c][v] || boxMap[(r/3)*3 + c/3][v]) return false;
                rowMap[r][v] = 1;
                colMap[c][v] = 1;
                boxMap[(r/3)*3 + c/3][v] = 1;
            }
        }
        return true;
    }
};
