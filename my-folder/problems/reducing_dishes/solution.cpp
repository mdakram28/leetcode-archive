class Solution {
public:
    int maxSatisfaction(vector<int>& sat) {
        sort(sat.begin(), sat.end(), greater<>());

        int currTotal = 0;
        int currSat = 0;
        for (auto s: sat) {
            currTotal += s;
            if (currSat+currTotal > currSat) {
                currSat += currTotal;
            } else {
                break;
            }
        }
        return currSat;
    }
};