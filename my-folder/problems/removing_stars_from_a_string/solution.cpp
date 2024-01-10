class Solution {
public:
    string removeStars(string s) {
        std::string ret;
        for (char c: s) {
            if (c=='*') {
                ret.pop_back();
            } else {
                ret.push_back(c);
            }
        }
        return ret;
    }
};