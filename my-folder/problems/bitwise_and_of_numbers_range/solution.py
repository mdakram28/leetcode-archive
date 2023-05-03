class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left = bin(left)
        right = bin(right)
        if len(right) > len(left):
            left = "0"*(len(right)-len(left)) + left
        else:
            right = "0"*(len(left)-len(right)) + right
        
        ans = 0
        changed = False
        for a, b in zip(left, right):
            if changed or a != b:
                changed = True
                ans <<= 1
            else:
                if a == "1":
                    ans = (ans << 1) | 1
                else:
                    ans <<= 1

        return ans