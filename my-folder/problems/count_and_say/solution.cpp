class Solution {
public:
    string countAndSay(int n) {
        if(n==1) return "1";
        string s = countAndSay(n-1);
        string ret = "";
        int l = s.length();
        int i = 1;
        int start = 0;
        while(i < l) {
            if(s[i] != s[i-1]) {
                ret += to_string(i-start);
                ret += s[i-1];
                start = i;
            }
            i++;
        }
        ret += to_string(i-start);
        ret += s[i-1];
        return ret;
    }
};