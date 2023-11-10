class Solution {
public:
    int countPairs(vector<vector<int>>& coordinates, int k) {
        int total = 0;
        map<pair<int, int>, int> f;
        for (auto &v2: coordinates)
        {
            pair<int, int> p2 = {v2[0], v2[1]};
            
            for (int a=0; a<=k; a++)
            {
                int b = k-a;
                pair<int, int> p1 = {a^p2.first, b^p2.second};
                if (f.count(p1) > 0)
                    total += f[p1];
            }
            f[p2] += 1;
        }
        return total;
    }
};