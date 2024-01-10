class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0, j=0;
        std::string ret;
        while (i < word1.length() && j < word2.length()) {
            ret.push_back(word1[i++]);
            ret.push_back(word2[j++]);
        }

        while (i < word1.length()) {
            ret.push_back(word1[i++]);
        }

        while (j < word2.length()) {
            ret.push_back(word2[j++]);
        }

        return ret;
    }
};