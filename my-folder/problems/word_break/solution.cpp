class Solution {
public:
    bool wordBreak(string s, vector<string> &wordDict) {
        auto numWords = wordDict.size();
        auto dpSize = s.size() + 1;
//        vector<int> wordLength(numWords);
        vector<int> numWordsOfLength(22);
        vector<bool> dp(dpSize);

        for (int i = 0; i < numWords; i++) {
//            wordLength[i] = (int) wordDict[i].size();
            numWordsOfLength[wordDict[i].size()]++;
        }

        dp[0] = true;
        for (int wordEnd = 1; wordEnd < dpSize; wordEnd++) {
            int wordLengthLimit = min(20, wordEnd);
            for (int backWordLength = 1; backWordLength <= wordLengthLimit; backWordLength++) {
                int wordStart = wordEnd - backWordLength;
                if (dp[wordStart] && numWordsOfLength[backWordLength]) {

                    for (int wordIndex = 0; wordIndex < numWords; wordIndex++) {
                        if (wordDict[wordIndex].size() == backWordLength) {

                            bool isEqual = true;
                            for (int i = 0; i < backWordLength; i++) {
                                if (wordDict[wordIndex][i] != s[wordStart + i]) {
                                    isEqual = false;
                                    break;
                                }
                            }

                            if (isEqual) {
                                dp[wordEnd] = true;
                            }

                        }
                    }


                }
            }
        }

        return dp[dpSize - 1];
    }
};