from vehicle_type import Car
from vehicle_type import Motorcycle
from vehicle_type import Truck

class VehicleFactory:
    def manufacture_vehicle(self, vehicle_type):
        # Create and return a Car instance
        if vehicle_type == "car":
            return Car()  
        # Create and return a Motorcycle instance
        elif vehicle_type == "motorcycle":
            return Motorcycle()  
        # Create and return a Truck instance
        elif vehicle_type == "truck":
            return Truck()  
        # Raise an error for invalid vehicle types
        else:
            raise ValueError("Invalid vehicle type.")  