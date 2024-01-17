class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> count;
        std::unordered_map<int, int> countCount;
        for(int val: arr) {
            countCount[count[val]]--;
            count[val]++;
            countCount[count[val]]++;
        }

        for(auto &[c, cc]: countCount) {
            cout << c << ", " << cc << endl;
            if (cc > 1) return false;
        }

        return true;
    }
};