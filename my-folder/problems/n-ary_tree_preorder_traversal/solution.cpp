/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ret;
        addNode(root, ret);
        return ret;
    }
    
    void addNode(Node *node, vector<int> &vec) {
        if(node == nullptr) return;
        vec.push_back(node->val);
        int s = node->children.size();
        for(int i=0;i<s;i++) {
            addNode(node->children[i], vec);
        }
    }
};