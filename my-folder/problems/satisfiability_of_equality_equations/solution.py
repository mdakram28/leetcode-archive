class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # graph = [[] for _ in range(26)]
        groups = [i for i in range(26)]

        def group_rep(at):
            rep = at
            l = 0
            while groups[rep] != rep:
                rep = groups[rep]
                l += 1
            while at != rep:
                next_at = groups[at]
                groups[at] = rep
                at = next_at
            return rep, l
        

        for eq in equations:
            if eq[1] == '=':
                n1 = ord(eq[0])-ord('a')
                n2 = ord(eq[3])-ord('a')
                rep1, l1 = group_rep(n1)
                rep2, l2 = group_rep(n2)
                if l1 < l2:
                    groups[rep1] = rep2
                else:
                    groups[rep2] = rep1
        # print(groups)
        for eq in equations:
            if eq[1] == '!':
                n1 = ord(eq[0])-ord('a')
                n2 = ord(eq[3])-ord('a')
                if group_rep(n1)[0] == group_rep(n2)[0]:
                    return False
        
        return True


