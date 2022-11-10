class Solution {
public:
    string makeGood(string s) {
        int top = 0;
        int l = s.length();
        for(int i=1;i<l;i++) {
            if(top<0 || abs(s[i]-s[top]) != 32) {
                s[++top] = s[i];
            } else {
                top--;
            }
        }
        s.resize(top+1);
        return s;
    }
};