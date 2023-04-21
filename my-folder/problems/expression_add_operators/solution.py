class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        PLUS = 1
        MINUS = -1
        MUL = 2
        # SKIP = 0

        digs = [int(val) for val in num]
        nums = [int(num[0])]
        signs = [PLUS]
        n = len(num)
        ans = []

        SIGN = {1: '+', -1: '-', 2: '*'}

        def dfs(i):
            if i < n:
                if nums[-1]:
                    nums[-1] = nums[-1]*10 + digs[i]
                    dfs(i+1)
                    nums[-1] //= 10
                nums.append(digs[i])
                signs.append(PLUS)
                dfs(i+1)
                signs.pop()
                signs.append(MINUS)
                dfs(i+1)
                signs.pop()
                signs.append(MUL)
                dfs(i+1)
                signs.pop()
                nums.pop()
            else:
                total = 0
                curr = 0
                for sign, num in zip(signs, nums):
                    if sign == PLUS or sign == MINUS:
                        total += curr
                        curr = num * sign
                    else:
                        curr = curr*num
                total += curr
                if total == target:
                    s = [str(nums[0])]
                    for sign, num in zip(signs[1:], nums[1:]):
                        s.append(SIGN[sign])
                        s.append(str(num))
                    ans.append(''.join(s))
        
        dfs(1)
        return ans