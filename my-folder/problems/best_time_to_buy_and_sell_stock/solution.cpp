class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if (size <= 1) return 0;
        int minValue = prices[0];
        int profit = 0;
        for(int i=1;i<size;i++) {
            if (prices[i]-minValue > profit) {
                profit = prices[i]-minValue;
            } else if (prices[i] < minValue) {
                minValue = prices[i];
            }
        }
        return profit;
    }
};