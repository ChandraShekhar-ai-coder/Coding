class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def Car_Details(self):
        print("--- Car Details ---\n")
        print(f"Car's Brand    : {self.brand}")
        print(f"Car's Color  : {self.color}")

if __name__ == "__main__":
 car1 = car("Rahul Sharma", "2026BTCS042")
 car1.Car_Details()
        