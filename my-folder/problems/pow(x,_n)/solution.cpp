class Solution {
public:
    double myPow(double x, int n) {
        uint64_t t = n;
        if (n < 0) {
            t = abs(n);
            x = 1/x;
        }
        double mul = x;
        double result = 1;
        while(t) {
            // cout << t << ", " << mul << endl;
            if (t&1) {
                result *= mul;
            }
            t >>= 1;
            mul *= mul;
        }
        return result;
    }
};