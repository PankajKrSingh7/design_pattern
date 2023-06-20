from vehicle import Vehicle

# Initialize the Car with 4 wheels, 5 seating capacity, and a max speed of 200
class Car(Vehicle):
    def __init__(self):
        super().__init__(4, 5, 200) 
        

# Initialize the Motorcycle with 2 wheels, 1 seating capacity, and a max speed of 180
class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(2, 1, 180)  


# Initialize the Truck with 6 wheels, 3 seating capacity, and a max speed of 150
class Truck(Vehicle):
    def __init__(self):
        super().__init__(6, 3, 150)  