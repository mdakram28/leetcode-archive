
struct TrieNode {
    std::unordered_map<char, TrieNode*> children;
    bool isEnd = false;
    void insert(std::string &word) {
        auto node = this;
        for(char c: word) {
            if (!node->children[c]) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool find(std::string &word, bool matchEnd) {
        auto node = this;
        for(int i=0; i<word.size() && node; i++) {
            node = node->children[word[i]];
        }
        return node != nullptr && (!matchEnd || node->isEnd);
    }

    ~TrieNode() {
        for(auto &[c, next]: children) {
            delete next;
        }
    }
};


class Trie {
    TrieNode *root;
public:
    Trie() {
        root = new TrieNode();
    }

    ~Trie() {
        delete root;
    }
    
    void insert(string word) {
        root->insert(word);
    }
    
    bool search(string word) {
        return root->find(word, true);
    }
    
    bool startsWith(string prefix) {
        return root->find(prefix, false);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */