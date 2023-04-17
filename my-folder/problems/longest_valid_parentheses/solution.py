class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        # n = len(s)
        max_l = 0
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif len(st) > 1:
                st.pop()
                max_l = max(max_l, i - st[-1])
            else:
                st.pop()
                st.append(i)
        
        return max_l