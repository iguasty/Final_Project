

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
            
class MajorDeviceError(Exception):
    def __init__(self, message="A device error has occured, please restart device or consult user manual."):
        super().__init__()
        self.message = message