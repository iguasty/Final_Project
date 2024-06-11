import device

class Camera(device.Device):
    """Camera (inherited Device)"""
    def __init__(self,type="Camera", brand="Nikon", message="Take Picture!"):
        super().__init__(type, brand, message)
        self.type = type
        self.brand = brand
        self.message = message
    
    def power_on(self):
        """Turn on camera"""
        print("Powering on!")
        self.shutter_pictures()
    
    def shutter_pictures(times=5):
        """Takes pictures recursively, specified number of times."""
        if times <= 0:
            return
        print("Click!")
        Camera.shutter_pictures(times - 1)