class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length()-1;
        int len = s.length();
        while(l<len && !iswalnum(s[l])) l++;
        while(r>=0 && !iswalnum(s[r])) r--;
        while(l<r) {
            cout << l << "," << r << endl;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
            while(!iswalnum(s[l])) l++;
            while(!iswalnum(s[r])) r--;
        }
        return true;
    }
};