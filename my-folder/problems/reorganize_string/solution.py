
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        freq_sorted = []
        for c, f in freq.items():
            freq_sorted.append((f, c))
        freq_sorted.sort()

        max_char_f, max_char = freq_sorted.pop()
        
        ll_head = 0
        ll_val  = [max_char for i in range(max_char_f)]
        ll_next = [i+1 for i in range(max_char_f)]
        ll_next[-1] = "#"

        def ll_to_str():
            node = ll_head
            c = []
            while node != '#':
                c.append(ll_val[node])
                node = ll_next[node]
            return ''.join(c)

        node = ll_head
        f, c = 0, '$'
        while node != "#":
            if f == 0:
                if len(freq_sorted) == 0:
                    if ll_next[node] == '#':
                        break
                    else:
                        return ""
                else:
                    f, c = freq_sorted.pop()
                    # print(f"Switching to new char : {f}, {c}")

            new_idx = len(ll_val)
            ll_val.append(c)
            ll_next.append(ll_next[node])
            ll_next[node] = new_idx
            node = ll_next[new_idx]
            f -= 1
        
        if f > 0:
            freq_sorted.append((f, c))

        for f, c in freq_sorted[::-1]:
            # print(f"Filling new char : {f}, {c}")
            node = ll_head
            for i in range(f):
                new_idx = len(ll_val)
                ll_val.append(c)
                ll_next.append(ll_next[node])
                ll_next[node] = new_idx
                node = ll_next[new_idx]
        

        return ll_to_str()
        
        