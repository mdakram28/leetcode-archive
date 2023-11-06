// 
// 3 -> 1 -> 4 -> 2
//      ^---------+

#define DEBUG(var) cout << #var << " = " << var << endl;
#define DEBUG2(v1, v2) cout << #v1 << " = " << v1 << ", " << #v2 << " = " << v2 << endl;

int parent[1001];
int edgei[1001];

class Solution {
public:
    inline void reserve(int n)
    {
        memset(&parent, 0, sizeof(int) * n);
    }
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        auto n = edges.size();

        reserve(n+1);
        
        // cout << "n = " << n << endl;
        int pivot=0, p1=0, p2=0;
        for(auto &edge: edges)
        {
            const int p = edge[0], c = edge[1];
            if (parent[c])
            {
                // Cycle
                p1 = parent[c];
                p2 = p;
                pivot = c;
                continue;
            }
            parent[c] = p;
        }

        if (p1)
        {
            int node = p1;
            while(node != pivot && parent[node])
            {
                node = parent[node];
            }
            if (node == pivot)
                return {p1, pivot};
            return {p2, pivot};
        }

        // Stage 2:


        int node = 1;
        int p;
        while((p = parent[node]) > 0)
        {
            parent[node] = -p;
            node = p;
        }

        pivot = node;
        // cout << "pivot node = " << pivot << endl;

        for(int i=n-1; i>=0; i--)
        {
            // edgei[] = i;
            if(parent[edges[i][1]] < 0) 
            {
                return edges[i];
            }
        }

        return {0, 0};
    }
};