class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x0 = coordinates[0][0];
        int y0 = coordinates[0][1];
        int x1 = coordinates[1][0];
        int y1 = coordinates[1][1];

        int n1 = y1-y0, d1=x1-x0;

        int n = coordinates.size();
        for(int i=1; i<n; i++) {
            int xi = coordinates[i][0];
            int yi = coordinates[i][1];
            if( (n1*(xi-x0)) != (d1*(yi-y0)) ) return false;
        }
        return true;
    }
};