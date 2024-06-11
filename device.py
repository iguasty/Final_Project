

class Device:
    """Define basic device appliance"""
    def __init__(self, type="Device", brand="Brand", message="Blank message"):
        self.type = type
        self.brand = brand
        self.message = message
        
    def __str__(self):
        """Print out attributes of self"""
        return f"   Device type: {self.type}\n   Brand: {self.brand}\n   Message: {self.message}\n"
    
    def power_on(self):
        """Power on method"""
        print("Powering on!")
        return True
        
    
    # def input_time(self):
    #     """Input time for kitchen appliance"""
    #     bad_input = True
        
    #     while bad_input:
    #         try:
    #             time = input("Enter a valid time (seconds) ->")
    #             time = int(time)
    #             bad_input = False
    #         except ValueError as ve:
    #             print(f"That is not a valid time!")
                
    #     print(f"You entered {time} seconds!")
            
class MajorDeviceError(Exception):
    def __init__(self, message="A device error has occured, please restart device or consult user manual."):
        super().__init__()
        self.message = message