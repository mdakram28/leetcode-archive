class Solution {
public:
    int reverse(int64_t x) {
        uint64_t ret = 0;
        int sign = x < 0 ? -1 : 1;
        x = sign * x;
        uint64_t limit;
        if (sign == -1) {
            limit = 0b10000000000000000000000000000000l;
        } else {
            limit = 0b01111111111111111111111111111111l;
        }
//        cout << "limit=" << limit << endl;

        while (x > 0) {
            ret = (ret * 10) + (x % 10);
            x /= 10;
            if (ret > limit) {
                return 0;
            }
//            cout << ret << endl;
        }

        return sign * (int) ret;
    }
};