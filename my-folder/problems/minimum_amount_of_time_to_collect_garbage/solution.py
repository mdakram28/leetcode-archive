class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.append(0)

        total = 0
        d1 = 0
        d2 = 0
        d3 = 0
        for g, d in zip(garbage, travel):

            c1 = g.count("M")
            if c1 > 0:
                total += d1 + c1
                d1 = 0
            
            c2 = g.count("P")
            if c2 > 0:
                total += d2 + c2
                d2 = 0

            c3 = g.count("G")
            if c3 > 0:
                total += d3 + c3
                d3 = 0

            d1 += d
            d2 += d
            d3 += d
        
        return total
