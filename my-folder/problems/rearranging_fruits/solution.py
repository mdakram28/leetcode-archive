class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        
        for num in basket1:
            f1[num] += 1
        
        for num in basket2:
            f2[num] += 1
        
        q1 = []
        q2 = []
        for val, f in f1.items():
            extra = max(f - f2[val], 0)
            if extra == 0: continue
            if extra%2:
                return -1
            q1.extend(repeat(val, extra//2))
        
        for val, f in f2.items():
            extra = max(f - f1[val], 0)
            if extra == 0: continue
            if extra%2:
                return -1
            q2.extend(repeat(val, extra//2))
        
        if len(q1) != len(q2): return -1
        
        q1.sort()
        q2.sort()
        
        min_val = min(min(basket1), min(basket2))
        ans = 0
        
        # while q1 and min(q1[-1], q2[-1]) > min_val*2:
        #     ans += min_val*2;
        #     q1.pop()
        #     q2.pop()
        
        # while q1:
        #     ans += 
        
        i, j = 0, 0
        while i < len(q1) and j < len(q2):
            if q1[i] < q2[j]:
                cost = q1[i]
                i += 1
                q2.pop()
            else:
                cost = q2[j]
                j += 1
                q1.pop()
            ans += min(min_val*2, cost)
        return ans