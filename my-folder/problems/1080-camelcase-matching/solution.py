class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        

        def match(a, b):
            i = 0
            for c in b:
                while i < len(a) and a[i] != c:
                    if 'A' <= a[i] <= 'Z':
                        return False
                    i += 1

                if i == len(a):
                    return False
                
                i+=1
            
            return a[i:].lower() == a[i:]
        
        return [match(q, pattern) for q in queries]
