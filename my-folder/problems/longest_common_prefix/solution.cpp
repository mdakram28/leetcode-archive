class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int l = strs.size();
        int ml = strs[0].length();
        for (string &s: strs) {
            if (s.length() < ml) {
                ml = s.length();
            }
        }
        
        
        for (int ci=0;ci<ml;ci++) {
            for (int si=1;si<l;si++) {
                if (strs[si][ci] != strs[0][ci]) {
                    return strs[si].substr(0, ci);
                }
            }
        }
        
        return strs[0].substr(0, ml);
    }
};