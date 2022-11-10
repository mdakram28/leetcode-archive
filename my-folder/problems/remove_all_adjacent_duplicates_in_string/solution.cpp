class Solution {
public:
    string removeDuplicates(string s) {
        char st[s.length()+1];
        int top = 0;
        st[0] = 0;
        int l = s.length();
        for(int i=0;i<l;i++) {
            if (st[top] == s[i]) {
                top--;
            } else {
                st[++top] = s[i];
            }
        }
        st[top+1] = 0;
        string ret(st+sizeof(char), top);
        return ret;
    }
};