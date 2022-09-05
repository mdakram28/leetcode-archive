class Solution {
public:
    bool isSubsequence(string s, string t) {
        int si=0, ti=0;
        int tl = t.length(), sl=s.length();
        while(ti < tl && si < sl) {
            if (s[si] == t[ti]) {
                si++;
            }
            ti++;
        }
        return si == sl;
    }
};