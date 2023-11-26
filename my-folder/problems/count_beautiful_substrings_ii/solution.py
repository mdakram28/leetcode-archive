def factors(num):
    f = 2
    while num > 1:
        if num%f == 0:
            yield f
            num //= f
        else:
            f += 1
        
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        GF = defaultdict(lambda: defaultdict(int))
        
        GF[0][1] += 1
        
        factcount = defaultdict(int)
        for f in factors(k):
            factcount[f] += 1
        k = 1
        for f, count in factcount.items():
            k *= f**(math.ceil(count/2))
        
        t = 0
        total = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                t += 1
                
            f = (2*t-i)
            g = t%k
            # print(i, t)
            # for g2 in GF.keys():
            #     if (g-g2)%k != 0: continue
            total += GF[g][f]
                # print(f"Found {GF[g2][f]} indexes with remainder {g2}")
            
            GF[g][f] += 1
        
        return total
        