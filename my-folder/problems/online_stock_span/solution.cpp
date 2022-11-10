class StockSpanner {
    stack<pair<int, int>> st;
    int i;
public:
    StockSpanner() {
        st.push(make_pair(INT_MAX, 0));
        i = 1;
    }
    
    int next(int price) {
        while(st.top().first <= price) {
            st.pop();
        }
        int ret = i - st.top().second;
        st.push(make_pair(price, i++));
        return ret;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */