class Solution {
public:
    int minFlips(int a, int b, int c) {
        int ans = 0;
        while (a || b || c) {
            if (c&1) {
                if (((a|b)&1) == 0) {
                    // printf("case 1 \n");
                    ans++;
                }
            } else {
                ans += (a&1) + (b&1);
                // printf("Case 2 : %d \n", a&1 + b&1);
            }
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return ans;
    }
};