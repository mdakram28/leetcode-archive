class Solution:
    @cache
    def numTilings(self, n: int, extra=False) -> int:
        return int(not (extra or bool(n))) if n<=0 else (self.numTilings(n-1, False) + (self.numTilings(n-1, True) if extra else (self.numTilings(n-2, True)*2+self.numTilings(n-2, False) )))%(10**9+7)