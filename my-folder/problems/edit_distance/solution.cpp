class Solution {
public:
    int minDistance(string word1, string word2) {
        const int l1 = word1.size();
        const int l2 = word2.size();

        std::vector<int> dp(l1+1);

        for(int c=1; c<= l1; c++) {
            dp[c] = c;
        }

        int prevVal, nextPrevVal;
        for(int r=1; r<=l2; r++) {
            prevVal = dp[0];
            dp[0]++;
            for(int c=1; c<=l1; c++) {
                nextPrevVal = dp[c];
                dp[c] = std::min(
                    dp[c-1]+1,
                    dp[c]+1
                );
                if (word1[c-1] == word2[r-1]) {
                    dp[c] = std::min(dp[c], prevVal);
                } else {
                    dp[c] = std::min(dp[c], prevVal+1);
                }
                prevVal = nextPrevVal;
            }

            // cout << "r = " << r << ": ";
            // for(int val: dp) {
            //     cout << val << ", ";
            // }
            // cout << endl;
        }

        return dp[l1];
    }
};