class Solution:
    def minDifficulty(self, diff: List[int], d: int) -> int:
        n = len(diff)

        @cache
        def cut_into(k, i):
            '''
            k : Cut into k parts
            i : Starting index of cut

            Returns : Min sum of cuts
            '''
            if k == 1: return max(diff[i:]) if i < n else float('inf')

            min_sum = float('inf')
            curr_diff = -float('inf')
            k -= 1
            for j in range(i, n-k):
                curr_diff = max(curr_diff, diff[j])
                min_sum = min(min_sum, curr_diff + cut_into(k, j+1))
            
            # print(f"cuts={k+1}, from={i}, {min_sum=}")
            return min_sum

        ret = cut_into(d, 0)

        return -1 if ret == float('inf') else ret

