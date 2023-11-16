class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
        for f,t in zip(moveFrom, moveTo):
            if f == t: continue
            count[t] = count[t]+count[f]
            del count[f]
        
        # allstones = []
        # for pos, c in count.items():
        #     allstones.extend([pos]*c)
        return sorted(count.keys())