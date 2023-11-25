class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        inc_st = []
        dec_st = []
        def get_lim(i, l, r):
            j1 = bisect_left(inc_st, (l, 0))-1
            if j1 == -1: j1 = 0
            else: j1 = inc_st[j1][1]+1

            ds = dec_st[::-1]
            j2 = bisect_right(ds, (r, float('inf')))
            if j2 == len(ds): j2 = 0
            else: j2 = ds[j2][1]+1
            
            # print(inc_st, dec_st, l ,r, j1, j2)
            return max(j1, j2)
        
        total = 0
        for i, num in enumerate(nums):
            
            minj = i
            for l in range(num-2, num+1):
                r = l+2
                j = get_lim(i, l, r)
                # print(i, num, l, r, j)
                minj = min(minj, j)

            total += i-minj+1

            while inc_st and inc_st[-1][0] >= num:
                inc_st.pop()
            inc_st.append((num, i))

            while dec_st and dec_st[-1][0] <= num:
                dec_st.pop()
            if (not dec_st) or dec_st[-1][0] != num:
                dec_st.append((num, i))
        
        return total
            

