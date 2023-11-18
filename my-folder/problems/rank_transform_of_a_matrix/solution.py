class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        parent = {}
    
        def get_root(at):
            if at not in parent:
                parent[at] = at
                return at
            root = at
            while root != parent[root]:
                root = parent[root]
            while at != root:
                at, parent[at] = parent[at], root
            return root
        
        def merge(a, b):
            ra = get_root(a)
            rb = get_root(b)
            parent[ra] = rb
        
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            row = {}
            for c in range(n):
                val = matrix[r][c]
                if val in row:
                    merge((r,c), row[val])
                else:
                    get_root((r,c))
                row[val] = (r,c)
        
        for c in range(n):
            col = {}
            for r in range(m):
                val = matrix[r][c]
                if val in col:
                    merge((r,c), col[val])
                else:
                    get_root((r,c))
                col[val] = (r,c)
        
        maxinrow = defaultdict(int)
        maxincol = defaultdict(int)
        for root, children in groupby(sorted(
            (matrix[pos[0]][pos[1]], get_root(pos), pos) for pos in product(range(m), range(n))), 
            key=lambda x: x[1]):

            children = list(children)
            prev = 0
            for _, _, (r,c) in children:
                prev = max(prev, maxinrow[r], maxincol[c])
            for _, _, (r,c) in children:
                matrix[r][c] = prev+1
                maxinrow[r] = max(prev+1, maxinrow[r])
                maxincol[c] = max(prev+1, maxincol[c])
            # print(root, children, prev+1)
        

        return matrix
