import device

class Light(device.Device):
    """Light (inherited Device)"""
    def __init__(self,type="Light", brand="Samsung", message="Lumos!"):
        super().__init__(type, brand, message)
        self.type = type
        self.brand = brand
        self.message = message
    def power_on(self):
        """Turn on light"""
        print("Powering on!")
        if self.type == "Microwave":
            raise PowerOnError            #raises error
        return super().start_process()
        
class PowerOnError(device.Device):
    def __init__(self, message="A power error has occured, please turn on and off again or consult user manual."):
        super().__init__(message)