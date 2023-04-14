# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)

        q = Deque([(root, 0)])
        r = 0
        row = collections.defaultdict(list)
        while q:
            row.clear()
            for _ in range(len(q)):
                node, c = q.popleft()
                row[c].append(node.val)
                if node.left:
                    q.append((node.left, c-1))
                if node.right:
                    q.append((node.right, c+1))
            for c in range(min(row.keys()), max(row.keys())+1):
                row[c].sort()
                cols[c].extend(row[c])
            r += 1


        # def dfs(node, r, c):
        #     if node is None: return
        #     cols[c][r].append(node.val)
        #     dfs(node.left, r+1, c-1)
        #     dfs(node.right, r+1, c+1)

        # dfs(root, 0, 0)
        # # print(cols)
        # ret = []
        # col = min(cols.keys())
        # while cols[col]:
        #     col_vals = []
        #     for r in sorted(cols[col].keys()):
        #         vals = cols[col][r]
        #         vals.sort()
        #         col_vals.extend(vals)
        #     ret.append(col_vals)
        #     col += 1
        ret = []
        for c in range(min(cols.keys()), max(cols.keys())+1):
            ret.append(cols[c])
        
        return ret