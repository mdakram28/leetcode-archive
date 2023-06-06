class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0;
        int h = 0;
        for(int n: gain) {
            h += n;
            ans = max(ans, h);
        }
        return ans;
    }
};