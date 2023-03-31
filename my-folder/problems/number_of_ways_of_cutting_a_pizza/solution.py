class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows = len(pizza)
        cols = len(pizza[0])

        num_apples = [0] * (cols+1)
        cum_sum = [num_apples]
        # print(num_apples)
        for row in pizza:
            num_apples = [*num_apples]
            t = 0
            for c in range(1, len(row)+1):
                if row[c-1] == 'A':
                    t += 1
                num_apples[c] += t
            cum_sum.append(num_apples)
            # print(num_apples)


        def count_apples(r1, c1, r2, c2):
            return cum_sum[r1][c1] + cum_sum[r2+1][c2+1] - cum_sum[r1][c2+1] - cum_sum[r2+1][c1]
        
        @cache
        def get_ways(r, c, k):
            if count_apples(r, c, rows-1, cols-1) < k:
                return 0
            elif k == 1:
                return 1
            w = 0
            for cut_row in range(r+1, rows):
                if count_apples(r, c, cut_row-1, cols-1) == 0:
                    continue
                w += get_ways(cut_row, c, k-1)
             
            for cut_col in range(c+1, cols):
                if count_apples(r, c, rows-1, cut_col-1) == 0:
                    continue
                w += get_ways(r, cut_col, k-1)
            # print(f'get_ways({r=}, {c=}, {k=}) = {w}')
            return w%(10**9+7)
        
        return get_ways(0, 0, k)