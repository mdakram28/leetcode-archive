class Solution {
    unordered_map<long, int> cache;
public:
    int placeQueen(int r, long cused, long d1used, long d2used, int n) {
        if (r == n) return 1;

        long ckey = d1used << 27 | d2used << 9 | cused;
        if(cache.count(ckey)) return cache[ckey];

        int total = 0;
        for(int c=0; c<n; c++) {
            if (cused&(1<<c) || d1used&(1<<(n+c-r)) || d2used&(1<<(c+r))) continue;
            total += placeQueen(
                r+1,
                cused|(1<<c),
                d1used|(1<<(n+c-r)),
                d2used|(1<<(c+r)),
                n
            );
        }
        cache[ckey] = total;
        return total;
    }
    int totalNQueens(int n) {
        return placeQueen(0, 0, 0, 0, n);
    }
};