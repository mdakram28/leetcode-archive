class Solution {
public:
    string reverseWords(string s) {
        std::string rev;
        int i=0;
        rev.resize(s.size());

        for (int j=s.size()-2; j>=-1 ;j--) {
            if ((j==-1 || s[j] == ' ') && s[j+1] != ' ') {
                for(int k=j+1; k<s.size() && s[k] != ' '; k++) {
                    rev[i++] = s[k];
                }
                rev[i++] = ' ';
            }
        }

        rev.resize(i-1);

        return rev;
    }
};