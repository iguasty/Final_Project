import device

class Light(device.Device):
    """Light (inherited Device)"""
    def __init__(self,type="Light", brand="Samsung", message="Lightswitch"):
        super().__init__(type, brand, message)
        self.type = type
        self.brand = brand
        self.message = message
    def power_on():
        """Turn on light"""
        type = "Light"
        print("Powering on!")
        try:
            if type == "Light":
                raise PowerOnError    #raises error
            return super().power_on()
        except PowerOnError as pe:
            print(pe.message)
        
class PowerOnError(device.MajorDeviceError):
    def __init__(self, message="A power error has occured, please turn on and off again or consult user manual."):
        super().__init__(message)