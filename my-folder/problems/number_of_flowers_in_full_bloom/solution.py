class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ret = [0] * len(people)
        flowers.append([float('inf'), float('inf')])
        flowers.sort(reverse=True)

        rem_t = [float('inf')]

        count = 0
        for t, i in sorted((p, i) for i,p in enumerate(people)):
            while flowers[-1][0] <= t:
                rem_time = flowers.pop()[1]
                if rem_time >= t:
                    heappush(rem_t, rem_time)
                    count += 1
            while rem_t[0] < t:
                heappop(rem_t)
                count -= 1
            ret[i] = count
        
        return ret