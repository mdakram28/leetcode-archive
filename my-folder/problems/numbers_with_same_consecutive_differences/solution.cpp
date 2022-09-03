#ifdef LOCAL_RUN

#include <iostream>
#include <vector>
#include <numeric>
#include "util.h"

using namespace std;
#else
#define printVector(x)
#endif
// Solution Begin ----------

class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> vec;
        int current;
        int lastDigit;
        int minusDigit;
        int plusDigit;

        for (int i = 1; i <= 9; i++) {
            if (i - k >= 0 || i + k <= 9) {
                vec.push_back(i);
            }
        }

        if (k == 0) {
            for (int d = 2; d <= n; d++) {
                auto size = vec.size();
                for (int i = 0; i < size; i++) {
                    vec[i] = vec[i]*10 + (vec[i]%10);
                }
            }
        } else {
            for (int d = 2; d <= n; d++) {
                printVector(vec);
                auto size = vec.size();
                for (int i = 0; i < size; i++) {
                    current = vec[i];
                    lastDigit = current % 10;
                    minusDigit = lastDigit - k;
                    plusDigit = lastDigit + k;
                    if (minusDigit >= 0) {
                        vec[i] = current * 10 + minusDigit;
                        if (plusDigit <= 9) {
                            vec.push_back(current * 10 + plusDigit);
                        }
                    } else {
                        if (plusDigit <= 9) {
                            vec[i] = current * 10 + plusDigit;
                        }
                    }
                }
            }
        }
        printVector(vec);
        return vec;
    }
};

// Solution End --------------
#ifdef LOCAL_RUN


int main() {
    Solution sol;
    vector<vector<int>> inputs = {
            {3, 7},
            {2, 1}
    };
    vector<vector<int>> expecteds = {
            {181, 292, 707, 818, 929},
            {10,  12,  21,  23,  32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98}
    };
    for (int i = 0; i < inputs.size(); i++) {

        auto output = sol.numsSameConsecDiff(inputs[i][0], inputs[i][1]);
        sort(output.begin(), output.end());
        sort(expecteds[i].begin(), expecteds[i].end());

        if (expecteds[i] == output) {
            std::cout << i << " Matched" << endl;
        } else {
            std::cout << i << " Not Matched" << endl;
        }
    }

    return 0;
}

#endif