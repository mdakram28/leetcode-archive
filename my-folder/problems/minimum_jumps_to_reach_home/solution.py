class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = Deque([(0, True)])

        n = 6000
        can_jump_fw = [True] * n
        can_jump_bw = [True] * n
        jumps = 0

        can_jump_fw[0] = False
        can_jump_bw[0] = False
        for pos in forbidden:
            if pos < n:
                can_jump_fw[pos] = False
                can_jump_bw[pos] = False

        while q:
            for _ in range(len(q)):
                pos, is_back = q.popleft()

                if pos == x:
                    return jumps

                if pos+a < n and can_jump_fw[pos+a]:
                    can_jump_fw[pos+a] = False
                    q.append((pos+a, False))
                
                if is_back:
                    continue
                
                if 0 < pos-b and can_jump_bw[pos-b]:
                    can_jump_bw[pos-b] = False
                    q.append((pos-b, True))
            
            jumps += 1

        return -1