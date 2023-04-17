class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        @cache
        def end(i):
            j = i
            while j < n and candidates[j] == candidates[i]:
                j += 1
            return j
        
        ans = []
        st = []
        def recurse(i, t):
            if t == 0:
                ans.append([*st])
                return
            if i == n:
                return
            
            
            prev_st_size = len(st)
            next_i = end(i)

            recurse(next_i, t)
            c = candidates[i]
            for j in range(i, next_i):
                if c > t:
                    break
                st.append(c)
                t -= c
                recurse(next_i, t)

            while len(st) > prev_st_size:
                st.pop()

        recurse(0, target)
        return ans