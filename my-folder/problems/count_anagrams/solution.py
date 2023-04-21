def mod_inv(a, m): return pow(a, m-2, m)

def mod_div(a, b, m): return (mod_inv(b, m) * a) % m
    
class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        mod = 10**9+7
        
        fact = [1]
        for i in range(1, 10**5+1):
            fact.append((fact[-1]*i)%mod)
        
        for word in s.split(" "):
            
            freq = defaultdict(int)
            for c in word:
                freq[c] += 1
            
            den = 1
            for c, f in freq.items():
                if f: den = (den*fact[f])%mod
                    
            ans = (ans * mod_div(fact[len(word)], den, mod)) % mod
            
        return ans