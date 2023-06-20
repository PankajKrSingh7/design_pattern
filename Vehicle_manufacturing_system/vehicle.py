# vehicle class defining attributes
class Vehicle:
    def __init__(self, num_wheels, seating_capacity, max_speed):
        self.num_wheels = num_wheels
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed

    def display_details(self):
        print(f"Number of wheels: {self.num_wheels}")
        print(f"Seating capacity: {self.seating_capacity}")
        print(f"Maximum speed: {self.max_speed}")