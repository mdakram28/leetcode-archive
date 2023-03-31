class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [gas[i] - cost[i] for i in range(len(gas))]

        t = gas[0] - cost[0]
        min_t = t
        min_i = 0
        for i in range(1, len(gas)):
            t += gas[i] - cost[i]
            if t < min_t:
                min_t = t
                min_i = i
        
        return (min_i+1) % len(gas) if t >= 0 else -1