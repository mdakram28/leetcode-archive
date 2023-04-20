class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        prev = []

        def dfs(i, k, n):
            if k == 0:
                if n == 0:
                    ans.append([*prev])
                return
            elif n <= 0:
                return
            
            for j in range(i, min(10, n+1)):
                prev.append(j)
                dfs(j+1, k-1, n-j)
                prev.pop()
        
        dfs(1, k, n)
        return ans
