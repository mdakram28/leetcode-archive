class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row;
        row.push_back(1);
        while (rowIndex--) {
            row.push_back(0);
            for (int i=row.size()-1; i>0; i--) {
                row[i] = row[i] + row[i-1];
            }
        }
        return row;
    }
};