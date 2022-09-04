const int ALPHABET_SIZE = 26;

// trie node
struct TrieNode
{
    struct TrieNode *children[ALPHABET_SIZE];
    bool isEndOfWord;
};

class Trie {
    TrieNode *root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode *node = root;
        for(int i=0;i<word.length();i++) {
            int index = word[i] - 'a';
            if (node->children[index]) {
                node = node->children[index];
            } else {
                node->children[index] = new TrieNode();
                node = node->children[index];
            }
        }
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode *node = root;
        for(int i=0; i<word.length() && node!=nullptr; i++) {
            int index = word[i] - 'a';
            node = node->children[index];
        }
        return node!=nullptr && node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode *node = root;
        for(int i=0; i<prefix.length() && node!=nullptr; i++) {
            int index = prefix[i] - 'a';
            node = node->children[index];
        }
        return node!=nullptr;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */