class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if(find(wordList.begin(), wordList.end(), beginWord) == wordList.end()) {
            wordList.push_back(beginWord);
        }

        // for(auto w: wordList) {
        //     cout << w << ", ";
        // }
        // cout << endl;

        // int n = wordList.size();
        map<string, vector<string>> g;

        for(string &w1: wordList) {
            for(string &w2: wordList) {
                int diff = 0;
                for(int i=0; diff<=1 && i<w1.length() && i<w2.length(); i++) {
                    if (w1[i]!=w2[i]) diff++;
                }
                if (diff <= 1) {
                    g[w1].push_back(w2);
                }
            }
        }

        map<string, int> dist;
        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> q;
        dist[beginWord] = 1;
        q.push(make_pair(1, beginWord));

        while (q.size() > 0) {
            int d;
            string at;
            tie (d, at) = q.top();
            q.pop();
            d++;
            for(string &to: g[at]) {
                if (dist.find(to) == dist.end() || d < dist[to]) {
                    dist[to] = d;
                    q.push(make_pair(d, to));
                }
            }
        }

        // for(auto w: dist) {
        //     printf("%s : %d \n", w.first.c_str(), w.second);
        // }

        return dist[endWord] != INT_MAX ? dist[endWord] : 0;
    }
};