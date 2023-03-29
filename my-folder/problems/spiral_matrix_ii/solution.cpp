class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> m;
        for (int i=0;i<n;i++) {
            vector<int> row(n);
            m.push_back(row);
        }

        int top = 1, bottom = n-1, left = 0, right = n-1;
        int maxI = n*n;
        int r = 0, c = 0;
        int dir = 0;
        for(int i=1; i<=maxI; i++) {
            // printf("r=%d, c=%d\n", r, c);
            m[r][c] = i;
            switch(dir) {
                case 0: 
                    if (c == right) {
                        dir = (dir+1)%4;
                        r++;
                        right--;
                    } else c++;
                    break;
                case 1: 
                    if (r == bottom) {
                        dir = (dir+1)%4;
                        c--;
                        bottom--;
                    } else r++;
                    break;
                case 2: 
                    if (c == left) {
                        dir = (dir+1)%4;
                        r--;
                        left++;
                    } else c--;
                    break;
                case 3: 
                    if (r == top) {
                        dir = (dir+1)%4;
                        c++;
                        top++;
                    } else r--;
                    break;
            }
        }
        return m;
    }
};