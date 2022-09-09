class Solution {
public:
    string reverseWords(string s) {
        int length = s.length();
        int i=0;
        while(i<length) {
            int j=i;
            for(;j<length;j++) {
                if(s[j] == ' '){
                    break;
                } 
            }
            int l = i;
            int r = j-1;
            while(l<r) {
                char t = s[l];
                s[l] = s[r];
                s[r] = t;
                l++;
                r--;
            }
            i = j+1;
        }
        return s;
    }
};