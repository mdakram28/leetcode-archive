#define debug(var1) printf( #var1 "=%d\n", var1)
#define debug(var1,var2) printf( #var1 "=%d, " #var2 "=%d\n", var1, var2)
#define debug(var1,var2,var3) printf( #var1 "=%d, " #var2 "=%d, " #var3 "=%d\n", var1, var2, var3)

class Solution {
public:
    int mySqrt(int x) {
        long l = 0;
        long r = x/2;
        while(l<=r) {
            long mid = (l+r)/2;
            // debug(l, r, mid);
            if ((mid*mid) > x) {
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
        if ((l*l) > x) return l-1;
        else return l;
    }
};