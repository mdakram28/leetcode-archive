class Solution {
    int count1[26], count2[26];
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) return false;

        // memset(count1, 0, sizeof(count1));
        // memset(count2, 0, sizeof(count2));

        for(char c: word1) {
            count1[c-'a']++;
        }
        for(char c: word2) {
            count2[c-'a']++;
        }

        std::unordered_map<int, int> v1, v2;

        for(int i=0; i<26; i++) {
            if ((count1[i]==0) != (count2[i]==0)) return false;
            if (count1[i] > 0) {
                v1[count1[i]]++;
                v2[count2[i]]++;
            }
        }

        return v1 == v2;
    }
};