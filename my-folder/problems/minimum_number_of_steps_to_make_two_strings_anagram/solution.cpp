class Solution {
    int count1[26];
    int count2[26];
public:
    int minSteps(string s, string t) {
        for(char c: s) {
            count1[c-'a']++;
        }
        for(char c: t) {
            count2[c-'a']++;
        }
        int ans = 0;
        for(int i=0; i<26; i++) {
            if (count1[i] > count2[i]) ans += count1[i] - count2[i];
        }
        return ans;
    }
};