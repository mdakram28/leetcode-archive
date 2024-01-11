class StockSpanner {
std::vector<std::pair<int, int>> st = {{INT_MAX, -1}};
int i = 0;

public:
    StockSpanner() {
    }
    
    int next(int price) {
        while (st[st.size()-1].first <= price) {
            st.pop_back();
        }
        int ret = i-st[st.size()-1].second;
        st.push_back({price, i});
        i++;
        return ret;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */