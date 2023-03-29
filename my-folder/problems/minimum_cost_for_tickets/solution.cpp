class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int c1 = costs[0];
        int c7 = costs[1];
        int c30 = costs[2];

        vector<int> dp;
        // vector<int> dp7(365);
        // vector<int> dp30(365);
        dp.push_back(0);
        // dp7[0] = 0;
        // dp30[0] = 0;
        int last = 0;
        for(auto day : days) {
            while (dp.size() < day) {
                dp.push_back(last);
            }
            last = min({
                dp[day-1] + c1,
                dp[max(day-7, 0)] + c7,
                dp[max(day-30, 0)] + c30,
            });
            dp.push_back(last);
        }
        return last;
    }
};