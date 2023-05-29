class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.f = [None, self.f1, self.f2, self.f3]


    def addCar(self, carType: int) -> bool:
        return self.f[carType]()
    
    def false(self):
        return False

    def f1(self):
        if self.big == 0:
            self.f[1] = self.false
            return False
        self.big -= 1
        return True
    

    def f2(self):
        if self.medium == 0:
            self.f[2] = self.false
            return False
        self.medium -= 1
        return True
    

    def f3(self):
        if self.small == 0:
            self.f[3] = self.false
            return False
        self.small -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)