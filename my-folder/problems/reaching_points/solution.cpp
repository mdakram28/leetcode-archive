class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        int x = tx;
        int y = ty;
        
        while(x>=sx && y>=sy) {
            if(x > y) {
                x = x%y;
                if(y!=0 && (sx-x)%y == 0 && y==sy) return true;
            } else {
                y = y%x;
                if(x!=0 && (sy-y)%x == 0 && x==sx) return true;
            }
        }
        
        return (x==sx && y==sy);
    }
};