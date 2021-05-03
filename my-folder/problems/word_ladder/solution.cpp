class Solution {
    void check_nodes(int i, int d,
                     vector<vector<int>> &graph, 
                     vector<int> &distance) {
        if(d < distance[i]) {
            distance[i] = d;
            for(int &conn: graph[i]) {
                check_nodes(conn, d+1, graph, distance);
            }
        }
    }
    
    int word_diff(string &w1, string &w2) {
        int c = 0;
        for(int i=0;i<w1.length();i++) {
            if(w1[i] != w2[i]) {c++;}
        }
        return c;
    }
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        vector<int> row;
        vector<vector<int>> graph(wordList.size(), row);
        vector<int> distance(wordList.size(), INT_MAX);
        
        for(int i=0;i<wordList.size();i++) {
            
            for(int j=0;j<i;j++) {
                if(word_diff(wordList[i], wordList[j]) == 1) {
                    graph[j].push_back(i);
                    graph[i].push_back(j);
                }
            }
            
        }
        
        for(int i=0;i<wordList.size();i++) {
            if(word_diff(wordList[i], beginWord) == 1) {
                check_nodes(i, 1, graph, distance);
            }
        }
        
        // for(int i=0;i<wordList.size();i++) {
        //     cout << wordList[i] << "=" << distance[i] << "\t";
        // }
        // cout << endl;
        // for(int i=0;i<graph.size();i++) {
        //     cout << wordList[i] << " : ";
        //     for(int j=0;j<graph[i].size();j++) {
        //         cout << wordList[j] << ", " ;
        //     }
        //     cout << endl;
        // }
        
        for(int i=0;i<wordList.size();i++) {
            if(wordList[i] == endWord) {
                if(distance[i] == INT_MAX) return 0;
                else return distance[i]+1;
            }
        }
        
        return 0;
    }
};