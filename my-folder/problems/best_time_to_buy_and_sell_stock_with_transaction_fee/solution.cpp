class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        long a = 0, b = INT_MIN;
        for(int p: prices) {
            long a2 = b+p-fee;
            long b2 = a-p;
            if (a2 > a) a = a2;
            if (b2 > b) b = b2;
        }
        return a;
    }
};