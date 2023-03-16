class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for t in tokens:
            if t == '+':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 + op2)
            elif t == '-':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 - op2)
            elif t == '*':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 * op2)
            elif t == '/':
                op2 = st.pop()
                op1 = st.pop()
                res = op1 / op2
                st.append(int(res))
            else:
                st.append(int(t))
            # print(st)
        return st[-1]
