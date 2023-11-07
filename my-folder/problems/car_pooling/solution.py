class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        return all(t <= capacity for t in accumulate(d for p, d in sorted(chain.from_iterable(((p, n), (d, -n)) for n,p,d in trips))))
        
        
        
        