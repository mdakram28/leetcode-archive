class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)

        total = 0

        def LCM(a, b): 
            return (a*b)//math.gcd(a, b)
        
        for i in range(n):
            lcm = 1
            for j in range(i, n):
                lcm = LCM(lcm, nums[j])
                if lcm > k:
                    break
                elif lcm == k:
                    total += 1

        return total
            
            

            

                