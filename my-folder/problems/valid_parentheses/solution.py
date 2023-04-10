CLOSING = {
    '(': ')',
    '{' : '}',
    '[': ']'
}
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in CLOSING:
                st.append(CLOSING[c])
            elif not st or c != st.pop():
                return False
        return not st
