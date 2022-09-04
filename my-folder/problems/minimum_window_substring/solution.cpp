class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> tFreq(128);
        int totalFreq = 0;
        auto tSize = t.size();
        auto sSize = s.size();
//        vector<queue<int>> retPos(128);
        vector<int> retFreq(128);
//        int totalRetPosSize = 0;
        int subStrStart = -1;
        int minSubStrStart = 0, minSubStrEnd = 2147483647;

        for (int i = 0; i < tSize; i++) {
            tFreq[t[i]]++;
            totalFreq++;
        }

        int i = 0;
        int count = 0;
        for (; i < sSize; i++) {
            char c = s[i];
            if (tFreq[c]) {
                subStrStart = i;
                retFreq[c]++;
                i++;
                if (retFreq[c] == tFreq[c]) {
                    count += retFreq[c];
                }
                break;
            }
        }
//        for (; i < sSize; i++) {
//            char c = s[i];
//            retFreq[c]++;
//            if (retFreq[c] == tFreq[c]) {
//                count += retFreq[c];
//                if (count == totalFreq) {
//                    subStrEnd = i + 1;
//                    i++;
//                    break;
//                }
//            }
//        }
        if (subStrStart == -1) return "";
        minSubStrStart = subStrStart;
        minSubStrEnd = subStrStart+1;
        for (; i < sSize; i++) {
            char c = s[i];
            retFreq[c]++;
            if (tFreq[c]) {
                if (retFreq[c] == tFreq[c]) {
                    count += retFreq[c];
                    if(count == totalFreq) {
                        minSubStrEnd = i+1;
                    }
                }
                while (retFreq[s[subStrStart]] > tFreq[s[subStrStart]]) {
                    if (retFreq[s[subStrStart]] == tFreq[s[subStrStart]]) {
                        count -= retFreq[s[subStrStart]];
                    }
                    retFreq[s[subStrStart]]--;
                    subStrStart++;
                }
                if (count == totalFreq) {
                    if (i + 1 - subStrStart < minSubStrEnd - minSubStrStart) {
                        minSubStrEnd = i + 1;
                        minSubStrStart = subStrStart;
                    }
                }
            }
        }
        return count != totalFreq ? "" : s.substr(minSubStrStart, minSubStrEnd - minSubStrStart);
    }
};