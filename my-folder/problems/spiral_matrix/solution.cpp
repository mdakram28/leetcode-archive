class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int size = rows*cols;
        vector<int> ret(size);
        
        int r=0, c=0;
        int dr=0, dc=1;
        int minr=0, maxr=rows-1;
        int minc=0, maxc=cols-1;
        
        for(int i=0;i<size; i++) {
            printf("%d, %d \n", r, c);
            ret[i] = matrix[r][c];
            
            // Calculate next r,c
            int nr=r+dr, nc=c+dc;
            
            // Checkl if valid next r,c
            if (nc>maxc) {
                dc=0;
                dr = 1;
                minr+=1;
            } else if (nr>maxr) {
                dr=0;
                dc=-1;
                maxc-=1;
            } else if (nc<minc) {
                dc=0;
                dr=-1;
                maxr-=1;
            } else if (nr<minr) {
                dr=0;
                dc=1;
                minc+=1;
            }
            
            // Set next r,c
            r = r+dr, c=c+dc;
        }
        
        
        return ret;
    }
};