CLOSING = {
    '(': ')',
    '{' : '}',
    '[': ']'
}
class Solution:
    def isValid(self, s: str) -> bool:
        b1, b2, b3 = 0, 0, 0
        st = []
        for c in s:
            if c in ('(', '{', '['):
                st.append(c)
            else:
                if len(st) == 0 or c != CLOSING[st.pop()]:
                    return False

        return len(st) == 0