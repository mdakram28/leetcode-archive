from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c = dict(zip(foods, cuisines))
        self.r = dict(zip(foods, ratings))

        self.d = defaultdict(SortedList)
        for r, f, c in zip(ratings, foods, cuisines):
            self.d[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.c[food]
        r = self.r[food]
        prev = (-r, food)
        curr = (-newRating, food)

        self.d[c].pop(self.d[c].bisect_left(prev))
        self.d[c].add(curr)

        self.r[food] = newRating


    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
