import device

class Camera(device.Device):
    """Camera (inherited Device)"""
    def __init__(self,type="Camera", brand="Nikon", message="Say cheese!"):
        super().__init__(type, brand, message)
        self.type = type
        self.brand = brand
        self.message = message
    
    def power_on(self):
        """Turn on camera"""
        print("Powering on!")
    
    def take_picture(self):
        """Takes a picture"""
        print("3,2,1, Click!")