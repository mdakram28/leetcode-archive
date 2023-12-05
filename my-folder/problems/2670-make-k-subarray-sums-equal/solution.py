class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        rem = set(range(n))

        ans = 0
        while rem:
            at = next(iter(rem))
            group = []
            while at in rem:
                rem.remove(at)
                group.append(arr[at])
                at = (at+k)%n
            group.sort()

            # print(group)

            op = float('inf')
            right = sum(group)
            left = 0
            for i, num in enumerate(group):
                op = min(op, num*i-left + right-(len(group)-i)*num)
                left += num
                right -= num
            ans += op
        
        return ans
