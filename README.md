## Design_pattern


### Weather Monitoring System

* To meet the requirements of the weather monitoring system, the Observer design pattern can be used to establish a one-to-many relationship between the weather station (subject) and the display devices (observers).

* In this implementation, the WeatherStation class acts as the subject (publisher) responsible for maintaining a list of registered observers (display devices) and notifying them when new weather data is available.

* The DisplayDevice class is an abstract class defining the common interface for all display devices (observers).

* The concrete display devices (MobileAppDisplay, WebInterfaceDisplay, DesktopApplicationDisplay) inherit from the DisplayDevice class and implement the update() method to display the received weather data.

* By using the Observer pattern, new display devices can be added to the system by creating a new class that inherits from DisplayDevice and implementing the update() method without modifying the existing code of the weather station or other display devices.

* Likewise, display devices can unsubscribe from the weather station by calling the remove_observer() method.
 
<img width="572" alt="weathor_monitoring" src="https://github.com/PankajKrSingh7/design_pattern/assets/54628129/2e7ed015-e47b-4c0c-badc-e4e224a7f52f">

  

### Vehicle Manufacturing System

* To meet the requirements of the vehicle manufacturing system, the Factory Method design pattern can be used to encapsulate the vehicle creation logic and provide a way to create different types of vehicles based on the user's input.

* In this implementation, the Vehicle class acts as the product interface defining the common method get_details() to access and display the attributes of the manufactured vehicle. The concrete vehicle classes (Car, Motorcycle, Truck) inherit from Vehicle and provide their specific attribute values.
  
* The VehicleFactory class acts as the creator interface with the abstract method create_vehicle() to create the vehicle object. The concrete factory classes (CarFactory, MotorcycleFactory, TruckFactory) inherit from VehicleFactory and implement the create_vehicle() method to return the respective vehicle objects.
 
* The user provides input for the desired vehicle type, and based on that input, the corresponding factory is selected. The factory is then used to create the desired vehicle object, and its details are displayed using the get_details() method.

* This implementation allows for easy extensibility by adding new vehicle types and their respective factories without modifying the existing code.
* 
<img width="666" alt="vehicle_manufacturing" src="https://github.com/PankajKrSingh7/design_pattern/assets/54628129/8759d131-862b-48f5-b7c2-d9890b70e2c9">




