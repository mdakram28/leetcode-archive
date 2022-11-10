# Function to find modulo inverse of b. It returns
# -1 when inverse doesn't
# modInverse works for prime m
def modInverse(b,m):
    g = math.gcd(b, m)
    if (g != 1):
        # print("Inverse doesn't exist")
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)
 
 
# Function to compute a/b under modulo m
def modDivide(a,b,m):
    a = a % m
    inv = modInverse(b,m)
    if(inv == -1):
        return None
    else:
        return (inv*a) % m

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        l=len(s)
        h=0
        p1=1
        s=s[::-1]
        found=-1
        for i in range(k-1, -1, -1):
            val = ord(s[i]) - 96
            h = (h + val*p1) % modulo
            # print(f"char='{s[i]}', val={val}, p1={p1}, h={h}")
            if i>0:
                p1 = (p1*power) % modulo
        
        # _h = sum([(ord(s[j])-96)*(power**j) for j in range(k)]) % modulo
        # print(f"Expected hash = {_h}")
        if h == hashValue:
            found=0
            # return s[0:k][::-1]
        # print("-----------")
        # p2=1
        for i in range(k, len(s)):
            val = ord(s[i]) - 96
            val2 = ord(s[i-k]) - 96
            
            h = (h - val2*p1) % modulo
            h = (h * power) % modulo
            h = (h + val) % modulo
            
            # p2 = (p2*power) % modulo
            # h = modDivide(h, power, modulo)
            # print(f"char='{s[i]}', val={val}, p1={p1}, h={h}")
            
            # _h = sum([(ord(s[i+1-k+j])-96)*(power**j) for j in range(k)]) % modulo
            # print(f"Expected hash = {_h}")
            if h == hashValue:
                # return s[i+1-k:i+1][::-1]
                found=i+1-k
        return s[found:found+k][::-1]
            
            
            
            