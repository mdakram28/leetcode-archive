class Solution:
    def maxScore(self, NUMS: List[int]) -> int:
        N = len(NUMS)

        gcd = {}
        for i in range(N-1):
            for j in range(i+1, N):
                gcd[(i, j)] = math.gcd(NUMS[i], NUMS[j])

        score = defaultdict(int)
        q = [(0, tuple(NUMS), 0)]

        while q:
            # print(q)
            s, nums, ind = heappop(q)
            ind+=1

            for i in range(N-1):
                if nums[i] == 0: continue
                for j in range(i+1, N):
                    if nums[j] == 0: continue

                    new_s = s - ind * gcd[(i, j)]
                    new_nums = nums[:i] + (0,) + nums[i+1:j] + (0,) + nums[j+1:]
                    if new_s < score[new_nums]:
                        score[new_nums] = new_s
                        heappush(q, (new_s, new_nums, ind))
        # print(score)
        return -score[(0,)*N]