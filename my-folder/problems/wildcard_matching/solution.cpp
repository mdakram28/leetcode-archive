class Solution {
public:
    bool isMatch(string s, string p) {
        bool *prev = new bool[s.length()+1];
        bool *curr = new bool[s.length()+1];
        
        memset(prev, false, s.length()+1);
        prev[0] = true;
        
        for(int i=0;i<p.length();i++) {
            if(p[i] == '*') {
                bool matched = false;
                for(int j=0;j<=s.length();j++) {
                    if(prev[j]) {
                        matched = true;
                    }
                    curr[j] = matched;
                }
            } else if(p[i] == '?') {
                curr[0] = false;
                for(int j=1;j<=s.length();j++) {
                    curr[j] = prev[j-1];
                }
            } else {
                curr[0] = false;
                for(int j=1;j<=s.length();j++) {
                    curr[j] = p[i] == s[j-1] && prev[j-1];
                }
            }
            
            // cout<<p[i]<<" ";
            // for(int i=0;i<=s.length();i++) cout<<curr[i];
            // cout<<endl;
            
            bool *temp = prev;
            prev = curr;
            curr = temp;
        }
        return prev[s.length()];
    }
};