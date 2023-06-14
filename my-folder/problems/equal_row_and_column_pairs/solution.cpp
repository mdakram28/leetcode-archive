template<class T>
struct Node {
    unordered_map<T, Node*> next;
    int count;
};

template<class T>
class Trie {
    Node<T> *root;
public:
    Trie() {
        root = new Node<T>();
    }
    void add(vector<T> &vals) {
        Node<T> *at = root;
        for(T &val: vals) {
            if (at->next.find(val) == at->next.end()) {
                Node<T> *newNode = new Node<T>();
                at->next[val] = newNode;
                at = newNode;
            } else {
                at = at->next[val];
            }
        }
        at->count++;
    }
    int getCount(vector<T> &vals) {
        Node<T> *at = root;
        for(T &val: vals) {
            if (at->next.find(val) == at->next.end()) {
                return 0;
            } else {
                at = at->next[val];
            }
        }
        return at->count;
    }
};

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        Trie<int> t;
        for(auto row: grid) {
            t.add(row);
        }
        int total = 0;
        for(int c=0; c<grid[0].size(); c++) {
            vector<int> col;
            for(int r=0; r<grid.size(); r++) {
                col.push_back(grid[r][c]);
            }
            total += t.getCount(col);
        }
        return total;
    }
};