class Solution:
    def divisorGame(self, n: int) -> bool:
        
        def get_next_options(n):
            for i in range(1, n):
                if n%i == 0:
                    yield i

        @cache
        def can_bob_win(n):
            for i in get_next_options(n):
                if not can_alice_win(n-i):
                    return True
            return False

        @cache
        def can_alice_win(n):
            for i in get_next_options(n):
                if not can_bob_win(n-i):
                    return True
            return False
        
        return can_alice_win(n)