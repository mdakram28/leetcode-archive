class Solution:
    def simplifyPath(self, path: str) -> str:
        st = [""]
        for token in path.split('/'):
            if token == "." or token == "":
                continue
            elif token == "..":
                if len(st) > 1:
                    st.pop()
            else:
                st.append(token)
        
        if len(st) == 1:
            return "/"
            
        return '/'.join(st)