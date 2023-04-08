class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # opened = 0
        ret = [True] * len(s)
        st = []

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st:
                    st.pop()
                else:
                    ret[i] = False
        
        for i in st:
            ret[i] = False
        
        return ''.join(c for incl, c in zip(ret, s) if incl)
