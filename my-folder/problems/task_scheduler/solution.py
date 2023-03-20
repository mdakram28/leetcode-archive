class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        freq = list(freq.values())
        freq.sort(reverse=True)

        max_freq = freq[0]
        min_time = (max_freq-1) * n + max_freq
        time = max_freq

        # slots = (max_freq-1)*n

        i = 1
        while i<len(freq) and freq[i] == max_freq:
            min_time += 1
            time += freq[i]
            i += 1
        
        while i < len(freq):
            time += freq[i]
            i += 1
        
        return max(min_time, time)