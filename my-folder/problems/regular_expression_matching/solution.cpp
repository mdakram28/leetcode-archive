class Solution {
public:
    inline bool matchOne(char c, char p) {
        return p == '.' || c == p;
    }
    
    bool isMatch(string s, string p) {
        vector<vector<bool>> M;
        vector<bool> firstRow(s.length()+1, false);
        firstRow[0] = true;
        M.push_back(firstRow);
        
        for (int r=1; r<=p.length(); r++) {
            vector<bool> row(s.length()+1);
            if (p[r-1] == '*') {
                if (r == 2) row[0] = true;
                else row[0] = M[r-2][0];
            }
            else row[0] = false;

            for (int c=1; c<=s.length(); c++) {
                if (p[r-1] == '*') {

                    // Match zero or more of prev character
                    row[c] = false;
                    int cp = c+1;

                    do {
                        cp--;
                        if (M[r-2][cp]) {
                            row[c] = true;
                            break;
                        }
                    } while (cp>0 && matchOne(s[cp-1], p[r-2]));

                } else {

                    // Match that chracter
                    row[c] = matchOne(s[c-1], p[r-1]) && M[r-1][c-1];

                }
            }
            // for(auto item: row) {
            //     cout << item << ", ";
            // }
            // cout << endl;
            M.push_back(row);
        }

        return M[p.length()][s.length()];
    }
};