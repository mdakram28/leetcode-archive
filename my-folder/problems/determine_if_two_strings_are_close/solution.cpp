template<typename K, typename V>
std::vector<V> values(std::unordered_map<K, V> m) {
    std::vector<V> ret;
    for(auto &p: m) {
        ret.push_back(p.second);
    }
    std::sort(ret.begin(), ret.end());
    return ret;
}

template<typename K, typename V>
std::vector<K> keys(std::unordered_map<K, V> m) {
    std::vector<K> ret;
    for(auto &p: m) {
        ret.push_back(p.first);
    }
    std::sort(ret.begin(), ret.end());
    return ret;
}

class Solution {
public:
    bool closeStrings(string word1, string word2) {
        std::unordered_map<char, int> f1;
        std::unordered_map<char, int> f2;

        for(char c: word1) f1[c]++;
        for(char c: word2) f2[c]++;

        return keys(f1) == keys(f2) && values(f1) == values(f2);
    }
};