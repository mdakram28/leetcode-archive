#ifdef LOCAL_RUN
#include "util.h"
#else
#define printVector(x)
#endif

// Solution Begin ----------
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> pos(129, -1);
        int start = -1;
        auto size = s.length();
        int largest = 0;
        int last_pos;
        for (int end = 0; end < size; end++) {
            char c = s[end];
            last_pos = pos[c];
            if (last_pos > -1) {
                while(start < last_pos) {
                    start++;
                    pos[s[start]] = -1;
                }
            } else {
                if ((end - start) > largest) {
//                    cout << "largest from " << start << " to " << end << endl;
                    largest = (end - start);
                }
            }
            pos[c] = end;
        }
        return largest;
    }
};
// Solution End --------------


#ifdef LOCAL_RUN
int main() {
    Solution sol;
    vector<string> inputs = {
            "tmmzuxt",
            "abcabcbb",
            "bbbbb",
            "pwwkew",
    };
    vector<int> expecteds = {
            5,
            3,
            1,
            3
    };
    for (int i = 0; i < inputs.size(); i++) {

        auto output = sol.lengthOfLongestSubstring(inputs[i]);

        if (expecteds[i] == output) {
            std::cout << i << " Matched" << endl;
        } else {
            std::cout << i << " Not Matched" << endl;
        }
    }

    return 0;
}

#endif