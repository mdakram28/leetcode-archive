class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        fr = []
        for c in s:
            if st and st[-1] == c:
                fr[-1] += 1
            else:
                st.append(c)
                fr.append(1)
            if fr and fr[-1] == k:
                st.pop()
                fr.pop()
        ret = []
        for c,f in zip(st, fr):
            ret.extend([c]*f)
        return ''.join(ret)