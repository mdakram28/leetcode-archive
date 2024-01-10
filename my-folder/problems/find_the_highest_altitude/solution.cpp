class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max = 0;
        int sum = 0;
        for (int i=0; i<gain.size(); i++) {
            sum += gain[i];
            max = std::max(max, sum);
        }
        return max;
    }
};