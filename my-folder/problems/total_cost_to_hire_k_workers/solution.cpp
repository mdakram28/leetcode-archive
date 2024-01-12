class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int cand) {
        int n = costs.size();
        int l = 0, r = n-1;
        std::priority_queue<int, std::vector<int>, std::greater<int>> lq, rq;

        while ((l <= r) && (lq.size() < cand || rq.size() < cand)) {
            if (lq.size() < cand) 
                lq.push(costs[l++]);
            if (l<=r && rq.size() < cand) 
                rq.push(costs[r--]);
        }
        
        long ans = 0;
        for(int i=0; i<k; i++) {
            if (rq.size() > 0 && lq.size() > 0) {
                if (rq.top() < lq.top()) {
                    ans += rq.top();
                    rq.pop();
                } else {
                    ans += lq.top();
                    lq.pop();
                }
                // cout << "from right: " << rq.top() << endl;
            } else if (lq.size() > 0) {
                // cout << "from left: " << lq.top() << endl;
                ans += lq.top();
                lq.pop();
            } else if (rq.size() > 0) {
                // cout << "from left: " << lq.top() << endl;
                ans += rq.top();
                rq.pop();
            }

            if (l<=r && lq.size() < cand) {
                lq.push(costs[l++]);
            }
            if (l<=r && rq.size() < cand) {
                rq.push(costs[r--]);
            }
        }
        return ans;
    }
};