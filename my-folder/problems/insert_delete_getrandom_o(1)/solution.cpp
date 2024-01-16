class RandomizedSet {
std::unordered_map<int, size_t> ind;
std::vector<int> vals;
public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (ind.contains(val)) return false;
        ind[val] = vals.size();
        vals.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!ind.contains(val)) return false;
        size_t i = ind[val];
        ind.erase(val);
        if (i == vals.size()-1) {
            vals.pop_back();
        } else {
            vals[i] = vals[vals.size()-1];
            ind[vals[i]] = i;
            vals.pop_back();
        }
        return true;
    }
    
    int getRandom() {
        size_t i = rand()%vals.size();
        return vals[i];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */