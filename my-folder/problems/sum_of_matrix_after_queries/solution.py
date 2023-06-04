class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        nq = len(queries)
        
        countr = 0
        countc = 0
        # rows_updated = [0] * nq
        # cols_updated = [0] * nq
        
        col_updated = [False] * n
        row_updated = [False] * n
        
        total = 0
        
        for qi in range(nq-1, -1, -1):
            # rows_updated[qi] = countr
            # cols_updated[qi] = countc
            
            if queries[qi][0] == 0:
                if row_updated[queries[qi][1]]: continue
                row_updated[queries[qi][1]] = True
                total += queries[qi][2] * (n-countc)
                countr += 1
            else:
                if col_updated[queries[qi][1]]: continue
                col_updated[queries[qi][1]] = True
                total += queries[qi][2] * (n-countr)
                countc += 1
            
        return total
        
        