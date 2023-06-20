## Peer Review - Jasveen Singh Kohli

### Vehicle (Abstract Class)
* This abstract class defines the interface for all types of vehicles.
* It contains an abstract method get_details() that must be implemented by concrete vehicle classes.
* Any new type of vehicle must inherit from this class and implement the required methods.

### Car, Motorcycle, Truck (Concrete Vehicle Classes)
* These classes represent different types of vehicles.
* They inherit from the Vehicle abstract class and provide their own implementations for the get_details() method.
* Each concrete vehicle class has specific attributes such as wheels, seating_capacity, and max_speed, which define the characteristics of the vehicle.

### VehicleFactory (Abstract Class)
* This abstract class defines the interface for creating vehicles.
* It contains an abstract method create_vehicle() that must be implemented by concrete factory classes.
* Any new type of vehicle factory must inherit from this class and implement the required methods.

### CarFactory, MotorcycleFactory, TruckFactory (Concrete Factory Classes)
* These classes represent concrete factories for creating specific types of vehicles.
* They inherit from the VehicleFactory abstract class and provide their own implementations for the create_vehicle() method.
* Each factory class is responsible for creating a specific type of vehicle object.
