class Solution {
public:
    void reverseString(vector<char>& s) {
        int size = s.size();
        int limit = size/2;
        size--;
        for(int i=0;i<limit;i++) {
            int t = s[i];
            s[i] = s[size-i];
            s[size-i] = t;
        }
    }
};