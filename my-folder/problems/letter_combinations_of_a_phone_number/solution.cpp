class Solution {
    string letters[10] = {
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    };
public:
    void add_all(string &s, int i, vector<char> &prev, vector<string> &ans) {
        if (i==s.length()) {
            ans.push_back(string(prev.begin(), prev.end()));
            return;
        }
        for (auto c: letters[s[i]-'0']) {
            prev.push_back(c);
            add_all(s, i+1, prev, ans);
            prev.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        vector<char> prev;
        if (digits.length() > 0) {
            add_all(digits, 0, prev, ans);
        }
        return ans;
    }
};