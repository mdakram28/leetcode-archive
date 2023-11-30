class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        @cache
        def make_00_from(n, d):
            mask = 1<<d
            bit = n&mask
            if mask == 0: return 0
            if mask == 1: return 1 if bit == 1 else 0
            if bit == 0:
                return make_00_from(n, d-1)
            else:
                return make_10_from(n, d-1) + 1 + make_00_from(1<<(d-1), d-1)
        
        @cache
        def make_10_from(n, d):
            mask = 1<<d
            bit = n&mask
            if mask == 0: return 0
            if mask == 1: return 1 if bit == 0 else 0
            if bit == 0:
                return make_10_from(n, d-1) + 1 + make_00_from(1<<(d-1), d-1)
            else:
                return make_00_from(n, d-1)
            
        
        return make_00_from(n, len(bin(n))-3)
        
