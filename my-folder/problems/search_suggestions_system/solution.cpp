
using NodeType = std::map<char, std::shared_ptr<void>>;
using NodePtr = std::shared_ptr<NodeType>;

NodePtr END_NODE = std::make_shared<NodeType>();
NodePtr root;

class Solution {

    void insert(std::string &word) {
        NodePtr node = root;
        for(char c: word) {
            // cout << "c = " << c << endl;
            if (node->find(c) == node->end()) {
                node->operator[](c) = std::make_shared<NodeType>();
            }
            node = std::static_pointer_cast<NodeType>(node->at(c));
        }
        node->operator[]('$') = END_NODE;
    }

    // std::shared_ptr<NodeType> find(std::shared_ptr<NodeType> node, std::string &prefix) {
    //     auto node = root;
    //     for(char c: prefix) {
    //         node = node->at(c);
    //         if (!node) return node;
    //     }
    //     return node;
    // }

    void addAll(const std::shared_ptr<NodeType> node, const std::string &prefix, std::vector<std::string> &v) {
        if (v.size() == 3) return;
        if (node->find('$') != node->end()) {
            // cout << "Adding " << prefix << endl;
            v.push_back(prefix);
        }
        // cout << "here " << endl;
        for(auto &[c, nextNode]: *node) {
            // cout << "c: " << c << endl;
            if (c=='$') continue;
            addAll(std::static_pointer_cast<NodeType>(nextNode), prefix+c, v);
        }
    }

public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        root = std::make_shared<NodeType>();
        for(std::string &word: products) {
            // cout << "inserting = " << word << endl;
            insert(word);
        }

        std::vector<std::vector<std::string>> ret(searchWord.size());

        auto node = root;
        std::string pref;
        for(char c: searchWord) {
            if (node->find(c) == node->end()) {
                return ret;
            }
            node = std::static_pointer_cast<NodeType>(node->at(c));
            pref += c;
            // cout << "c = " << c << endl;
            addAll(node, pref, ret[pref.size()-1]);
            // cout << "moved = " << c << endl;
        }

        return ret;
    }
};