class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x,y = 0,0
        maxbit = max(len(bin(a))-2, len(bin(b))-2, n)
        for i in range(maxbit-1, -1, -1):
            mask = 1<<i
            # print(a&mask, b&mask)
            if i >= n:
                x |= a&mask
                y |= b&mask
            elif a&mask==b&mask:
                x |= 1<<i
                y |= 1<<i
            else:
                if x < y:
                    x |= 1<<i
                else:
                    y |= 1<<i
                
        # print(x,y)
        return (x*y)%(10**9+7)