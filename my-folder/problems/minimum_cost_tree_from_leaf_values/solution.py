class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[None]*n for i in range(n)]
        
        def subProblem(i, j):
            if j-i == 1:
                return 0, arr[i]
            
            if dp[i][j-1] is None:

                min_sum = float('inf')
                max_leafval = None
                for mid in range(i+1, j):
                    left_sum, left_leafval = subProblem(i, mid)
                    right_sum, right_leafval = subProblem(mid, j)

                    curr_val = left_leafval * right_leafval
                    curr_sum = left_sum + right_sum + curr_val

                    if curr_sum < min_sum:
                        min_sum = curr_sum
                        max_leafval = max(left_leafval, right_leafval)
                dp[i][j-1] = (min_sum, max_leafval)

            return dp[i][j-1]
                
        return subProblem(0, len(arr))[0]

