struct hashFunction 
{ 
  size_t operator()(const pair<int ,  
                    int> &x) const
  {
    return x.first ^ x.second; 
  } 
};

class Solution {
public:
    bool isPathCrossing(string path) {
        unordered_set<pair<int, int>, hashFunction> visited;
        int cx = 0, cy = 0;

        visited.insert({cx, cy});

        for(char c: path)
        {
            switch(c)
            {
                case 'N': cy++; break;
                case 'S': cy--; break;
                case 'E': cx++; break;
                case 'W': cx--; break;
            }
            if (visited.find({cx, cy}) != visited.end())
            {
                return true;
            }
            visited.insert({cx, cy});
        }
        return false;
    }
};
