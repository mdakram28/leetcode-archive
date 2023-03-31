class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1, num2 = num2, num1
        l1, l2 = len(num1), len(num2)
        digs = []
        c = 0
        for i in range(min(l1, l2)):
            d1 = ord(num1[l1-i-1]) - ord('0')
            d2 = ord(num2[l2-i-1]) - ord('0')
            # print(d1, d2)
            digs.append((d1+d2+c)%10)
            c = (d1+d2+c) // 10
        
        if l1 > l2:
            for i in range(i+1, l1):
                d = ord(num1[l1-i-1]) - ord('0')
                # print("Extra", d)
                digs.append((d+c)%10)
                c = (d+c)//10
        else:
            for i in range(i+1, l2):
                d = ord(num2[l2-i-1]) - ord('0')
                # print("Extra", d)
                digs.append((d+c)%10)
                c = (d+c)//10
        
        if c > 0:
            digs.append(c)
        if len(digs) == 0:
            digs.append(0)
        return ''.join(map(str, digs[::-1]))