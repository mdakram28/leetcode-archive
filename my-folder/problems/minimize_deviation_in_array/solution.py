from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        nextvals = []
        for i, num in enumerate(nums):
            nextval = [num]
            c = 1
            if num&1 == 0:
                while num&1 == 0:
                    nextval.append(num>>1)
                    num >>= 1
                    c += 1
            else:
                nextval.append(num<<1)
                nextval.reverse()
                c += 1
            nextvals.append(nextval)
        
        
        q = [(nextval.pop(), i) for i, nextval in enumerate(nextvals)]

        heapify(q)
        maxval = max(q)[0]
        ans = maxval - q[0][0]
        
        while True:
            # print(maxval, q)
            ans = min(ans, maxval - q[0][0])

            minval, i = heappop(q)
            if len(nextvals[i]) == 0:
                break

            nextval = nextvals[i].pop()
            heappush(q, (nextval, i))
            if nextval > maxval:
                maxval = nextval
        
        return ans
