from fractions import Fraction
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def fn2(a, b):
            return (
                math.isclose(a * b, 24) or
                b and math.isclose(a / b, 24) or
                math.isclose(a + b, 24) or
                math.isclose(a - b, 24)
            )

        def fn3(a, b, c):
            return (
                fn2(a * b , c) or
                fn2(a , b * c) or

                b and fn2(a / b , c) or
                c and fn2(a , b / c) or

                fn2(a + b , c) or
                fn2(a , b + c) or

                fn2(a - b , c) or
                fn2(a , b - c)
            )

        # @cache
        def fn4(a, b, c, d):
            return (
                fn3(a * b , c , d) or
                fn3(a , b * c , d) or
                fn3(a , b , c * d) or

                b and fn3(a / b , c , d) or
                c and fn3(a , b / c , d) or
                d and fn3(a , b , c / d) or

                fn3(a + b , c , d) or
                fn3(a , b + c , d) or
                fn3(a , b , c + d) or
                
                fn3(a - b , c , d) or
                fn3(a , b - c , d) or
                fn3(a , b , c - d)
            )
        
        return any(fn4(*perm) for perm in itertools.permutations(cards))

