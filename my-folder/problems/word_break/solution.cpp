class TrieNode;

class TrieNode {
public:
    unordered_map<char, TrieNode*> child;
    bool is_end = false;
};

class Trie {
public:
    TrieNode root;
    void insert(string& word) {
        TrieNode* node = &root;
        for(char c : word) {
            TrieNode *nextNode = node->child[c];
            if (nextNode == nullptr) {
                nextNode = new TrieNode();
                node->child[c] = nextNode;
            }
            node = nextNode;
        }
        node->is_end = true;
    }
};

class Solution {
public:
    bool search(vector<vector<int>> &g, vector<bool> &visited, int target, int at) {
        if (at == target) return true;
        if (visited[at]) return false;
        visited[at] = true;

        for(int to : g[at]) {
            if (search(g, visited, target, to)) return true;
        }

        return false;
    }
    bool wordBreak(string s, vector<string>& wordDict) {
        Trie trie;
        for(auto word : wordDict) {
            trie.insert(word);
        }
        vector<vector<int>> g(s.length());
        vector<bool> visited(s.length());

        TrieNode* root = &trie.root;
        for(int i=0; i<s.length(); i++) {
            
            TrieNode* node = root;
            for(int j=i;; j++) {

                if (node->is_end) {
                    g[i].push_back(j);
                }

                if (j >= s.length() || node->child.find(s[j]) == node->child.end()) {
                    break;
                }
                node = node->child[s[j]];
            }

        }

        return search(g, visited, s.length(), 0);
    }
};