constexpr int MOD = 1000000007;

class Solution {
    long numWays(int n, int occ, std::unordered_map<size_t, long> &cache) {
        if (n < 0) return 0;
        else if (n == 0) return occ == 0 ? 1 : 0;

        size_t key = (n<<1) | occ;
        if (cache.find(key) != cache.end()) return cache[key];
        
        int ans = 0;
        switch(occ) {
            case 0: ans = (0l
                + numWays(n-1, 0, cache)
                + numWays(n-2, 0, cache)
                + numWays(n-1, 1, cache)*2
            )%MOD; break;
            case 1: ans = (0l
                + numWays(n-1, 1, cache)
                + numWays(n-2, 0, cache)
            )%MOD; break;
        }

        cache[key] = ans;
        return ans;
    }
public:
    int numTilings(int n) {
        std::unordered_map<size_t, long> cache;

        return numWays(n, 0, cache);
    }
};