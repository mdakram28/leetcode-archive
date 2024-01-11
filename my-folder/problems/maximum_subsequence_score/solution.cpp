class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        std::vector<std::pair<int, int>> pairs(nums1.size());
        for(int i=0; i<nums1.size(); i++) {
            pairs[i] = {nums2[i], nums1[i]};
        }

        std::sort(pairs.begin(), pairs.end(), std::greater());

        std::priority_queue<int, std::vector<int>, std::greater<int>> q;

        long total = 0;
        long ans = 0;
        for(auto [a, b]: pairs) {
            if (q.size() == k-1)
                ans = std::max(ans, (total+b)*a);

            total += b;
            q.push(b);
            // cout << "Added " << b << endl;
            if (q.size() > k-1) {
                total -= q.top();
                // cout << "Removed " << q.top() << endl;
                q.pop();
            }

        }
        return ans;
    }
};