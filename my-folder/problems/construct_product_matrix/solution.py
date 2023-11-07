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
        print("Division not defined")
    # else:
    #     print("Result of Division is ",)
    return (inv*a) % m
        
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        mod = 12345
        
        ret = [[1] * m for r in range(n)]
        
        prod = 1
        for r in range(n):
            for c in range(m):
                ret[r][c] = prod
                prod = (prod * grid[r][c])%mod
        
        prod = 1
        for r in range(n-1, -1, -1):
            for c in range(m-1, -1, -1):
                ret[r][c] = (ret[r][c] * prod) % mod
                prod = (prod * grid[r][c])%mod
                
        
        return ret
        
            
        
        
        
        
        
        
        
        
        
        
        