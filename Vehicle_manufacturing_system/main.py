from vehicle_factory import VehicleFactory

factory = VehicleFactory()

# Create a vehicle based on the user's input
vehicle_type = input("Enter the type of vehicle you want to manufacture (car, motorcycle, or truck): ")
vehicle = factory.manufacture_vehicle(vehicle_type)  

# Display the details of the created vehicle
print("Vehicle details:")
vehicle.display_details()  

