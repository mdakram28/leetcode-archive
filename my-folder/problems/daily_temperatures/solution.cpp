class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> st;
        std::vector<int> ans(temperatures.size());
        for (int i=0; i<temperatures.size(); i++) {
            while (st.size() > 0 && temperatures[st[st.size()-1]] < temperatures[i]) {
                ans[st[st.size()-1]] = i-st[st.size()-1];
                st.pop_back();
            }
            st.push_back(i);
        }
        for (auto i: st) {
            ans[i] = 0;
        }
        return ans;
    }
};