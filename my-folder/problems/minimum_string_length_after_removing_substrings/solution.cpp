class Solution {
public:
    int minLength(string s) {
        stack<char> st;
        st.push(0);
        
        for(auto c: s) {
            if (c == 'B' && st.top() == 'A') {
                st.pop();
            } else if (c == 'D' && st.top() == 'C') {
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.size()-1;
    }
};