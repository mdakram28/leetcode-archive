class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rep = list(range(n))
        edgeList.sort(key=lambda e: e[2])
        queries = sorted(enumerate(queries), key=lambda q: q[1][2])

        ans = [False] * len(queries)

        # print(rep)

        def get_rep(node):
            at = node
            while at != rep[at]:
                at = rep[at]
            g = at
            at = node
            while at != g:
                rep[at], at = g, rep[at]
            return g


        def merge(n1, n2):
            r1 = get_rep(n1)
            r2 = get_rep(n2)
            rep[r1] = r2
            # print("After merging", n1, n2, rep)

        ei = 0
        el = len(edgeList)

        for qi, [start, end, limit] in queries:
            while ei < el and edgeList[ei][2] < limit:
                merge(edgeList[ei][0], edgeList[ei][1])
                ei += 1
            # print(start, end, limit, rep)
            ans[qi] = get_rep(start) == get_rep(end)

        return ans