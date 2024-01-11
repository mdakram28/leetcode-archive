
#define DEBUG(var)      cout << #var << " = " << var << endl;

template<typename T1, typename T2>
ostream& operator<<(ostream& os, const std::pair<T1, T2> &p) {
    os << "{" << p.first << ", " << p.second << "}";
    return os;
}

template<typename T>
ostream& operator<<(ostream& os, const std::vector<T> &v) {
    for (auto &val: v)
        os << val << ", ";
    os << endl;
    return os;
}

template<typename T1, typename T2>
ostream& operator<<(ostream& os, const std::unordered_map<T1, T2> &m) {
    for (auto &[k, v]: m)
        os << k << ": " << v << ", ";
    os << endl;
    return os;
}

class Solution {
public:
    void dfs(
        int at, 
        int p,
        double prevProd,
        std::vector<std::vector<std::pair<int, double>>> &g,
        std::unordered_map<int, double> &prod) {
        if (prod.find(at) != prod.end()) return;
        prod[at] = prevProd;

        for (auto &[to, val]: g[at]) {
            if (to == p) {
                continue;
            }
            dfs(to, at, prevProd*val, g, prod);
        }
    }
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        std::unordered_map<std::string, int> id;
        std::vector<std::vector<std::pair<int, double>>> g;
        std::vector<double> ans(queries.size(), -1);

        for(int i=0; i<values.size(); i++) {
            if (id.find(equations[i][0]) == id.end()) {
                id[equations[i][0]] = id.size();
            }
            if (id.find(equations[i][1]) == id.end()) {
                id[equations[i][1]] = id.size();
            }
        }

        int n = id.size();
        g.resize(n);
        
        for(int i=0; i<values.size(); i++) {
            int a = id[equations[i][0]];
            int b = id[equations[i][1]];
            g[a].push_back({b, values[i]});
            g[b].push_back({a, 1/values[i]});
        }

        // DEBUG(g);
        
        std::vector<bool> seen(n);
        for (int i=0; i<n; i++) {
            if (seen[i]) continue;
            std::unordered_map<int, double> prod;
            dfs(i, -1, 1.0, g, prod);

            for(auto &[k, v]: prod) {
                seen[k] = true;
            }
            // DEBUG(prod);

            for(int i=0; i<queries.size(); i++) {
                if (id.find(queries[i][0]) == id.end() || id.find(queries[i][1]) == id.end()) {
                    continue;
                }
                int a = id[queries[i][0]];
                int b = id[queries[i][1]];
                if (prod.find(a) == prod.end() || prod.find(b) == prod.end()) {
                    continue;
                }
                ans[i] = prod[b]/prod[a];
            }

        }

        

        return ans;
    }
};