class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        groupA = list(range(n))
        groupB = list(range(n))

        def get_group(gr, a):
            at = a
            while at != gr[at]:
                at = gr[at]
            ans = at
            at = a
            while at != ans:
                gr[at], at = ans, gr[at]
            return ans

        def merge(gr, a, b):
            a = get_group(gr, a)
            b = get_group(gr, b)
            gr[a] = b
        
        ans = 0
        for t, u, v in edges:
            if t != 3: continue
            u -= 1
            v -= 1
            A_needs = get_group(groupA, u) != get_group(groupA, v)
            B_needs = get_group(groupB, u) != get_group(groupB, v)
            if A_needs or B_needs:
                if A_needs:
                    merge(groupA, u, v)
                if B_needs:
                    merge(groupB, u, v)
            else:
                # print((t, u, v) ,"is not needed")
                ans += 1
        
        for t, u, v in edges:
            if t == 3: continue
            u -= 1
            v -= 1
            gr = groupA if t == 1 else groupB
            if get_group(gr, u) != get_group(gr, v):
                merge(gr, u, v)
            else:
                # print((t, u, v),"is not needed")
                ans += 1
        
        gA = get_group(groupA, 0)
        gB = get_group(groupB, 0)
        for at in range(1, n):
            if get_group(groupA, at) != gA or get_group(groupB, at) != gB:
                return -1
        
        return ans


