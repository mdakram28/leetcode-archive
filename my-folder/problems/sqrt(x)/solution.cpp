class Solution {
public:
    int mySqrt(int x) {
        long long lo = 0;
        long long hi = INT_MAX;
        while (lo<hi) {
            long long mid = (lo+hi)/2;
            if ((mid*mid) < x) {
                lo = mid+1;
            } else if ((mid*mid) > x) {
                hi = mid;
            } else {
                return mid;
            }
        }
        return lo-1;
    }
};