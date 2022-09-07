class Solution {
public:
    int longestPalindrome(string s) {
        vector<int> freq(128);
        int size = s.length();
        for(int i=0; i<size;i++) {
            freq[s[i]]++;
        }
        
        int pal = 0;
        
        for(char i='A';i<='Z';i++) {
            pal += freq[i] / 2;
            pal += freq[i+32] / 2;
        }
        
        pal *= 2;
        if (size > pal) {
            return pal + 1;
        } else {
            return pal;
        }
    }
};