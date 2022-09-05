class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<bool> isMapKey(128);
        vector<bool> isMapValue(128);
        vector<char> map(128);

        if (s.size() != t.size()) return false;
        int size = s.size();
        for (int i = 0; i < size; i++) {
            if (!isMapKey[s[i]]) {
                if (isMapValue[t[i]]) return false;
                else {
                    map[s[i]] = t[i];
                    isMapKey[s[i]] = true;
                    isMapValue[t[i]] = true;
                }
            } else if (map[s[i]] != t[i]) {
                return false;
            }
        }
        return true;
    }
};