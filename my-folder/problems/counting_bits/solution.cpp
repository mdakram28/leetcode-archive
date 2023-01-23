class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ret(n+1);
        ret[0] = 0;
        if (n == 0) return ret;
        ret[1] = 1;
        for(int i=2;i<=n;i++) {
            ret[i] = ret[i>>1] + (i&1);
        }
        return ret;
    }
};