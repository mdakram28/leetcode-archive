const int ALPHABET_SIZE = 26;

// trie node
struct TrieNode {
    struct TrieNode *children[ALPHABET_SIZE];
    string *word;
};

class Trie {
public:
    TrieNode *root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string &word) {
        TrieNode *node = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word[i] - 'a';
            if (node->children[index]) {
                node = node->children[index];
            } else {
                node->children[index] = new TrieNode();
                node = node->children[index];
            }
        }
        node->word = &word;
    }

    bool search(string word) {
        TrieNode *node = root;
        for (int i = 0; i < word.length() && node != nullptr; i++) {
            int index = word[i] - 'a';
            node = node->children[index];
        }
        return node != nullptr && node->word;
    }

    bool startsWith(string prefix) {
        TrieNode *node = root;
        for (int i = 0; i < prefix.length() && node != nullptr; i++) {
            int index = prefix[i] - 'a';
            node = node->children[index];
        }
        return node != nullptr;
    }

    void printTrie(char c, const std::string &prefix, const TrieNode *node, bool isLeft) {
        std::cout << prefix;
        std::cout << (isLeft ? "├──" : "└──");
        // print the value of the node
        std::cout << c << std::endl;
        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (node->children[ch - 'a']) {
                bool isLeft2 = false;
                for(char ch2 = ch+1; ch2<='z'; ch2++) {
                    if (node->children[ch2 - 'a']) {
                        isLeft2 = true;
                        break;
                    }
                }
                printTrie(ch, prefix + (isLeft ? "│   " : "    "), node->children[ch - 'a'], isLeft2);
            }
        }
    }
};

class Solution {
    vector<string> ret;
    vector<vector<char>> board;
    size_t rows;
    size_t cols;
    bool visited[12][12];
public:
    vector<string> findWords(vector<vector<char>> &b, vector<string> &words) {
        Trie trie;
        ret.clear();
        board = b;
        // vector<vector<bool>> _visited(12);
        // visited = _visited;

        for (string &word: words) {
            trie.insert(word);
        }
        rows = board.size();
        cols = board[0].size();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                visited[r][c] = false;
            }
        }

//        trie.printTrie('*', "", trie.root, false);

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (trie.root->children[board[r][c] - 'a']) {
                    addAllWordsFrom(r, c, trie.root->children[board[r][c] - 'a']);
                }
            }
        }
        return ret;
    }

    void addAllWordsFrom(int r, int c, TrieNode *node) {
        if (visited[r][c]) return;
        if (node->word) {
            ret.push_back(*node->word);
            node->word = nullptr;
        }
        visited[r][c] = true;

        if (r > 0 && node->children[board[r - 1][c] - 'a']) {
            addAllWordsFrom(r - 1, c, node->children[board[r - 1][c] - 'a']);
        }
        if (r < rows - 1 && node->children[board[r + 1][c] - 'a']) {
            addAllWordsFrom(r + 1, c, node->children[board[r + 1][c] - 'a']);
        }
        if (c > 0 && node->children[board[r][c - 1] - 'a']) {
            addAllWordsFrom(r, c - 1, node->children[board[r][c - 1] - 'a']);
        }
        if (c < cols - 1 && node->children[board[r][c + 1] - 'a']) {
            addAllWordsFrom(r, c + 1, node->children[board[r][c + 1] - 'a']);
        }
        visited[r][c] = false;
    }
};