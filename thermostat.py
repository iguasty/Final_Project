import device

class Thermostat(device.Device):
    """Thermostat (inherited Device)"""
    def __init__(self,type="Thermostat", brand="LG", message="Set Temperature"):
        super().__init__(type, brand, message)
        self.type = type
        self.brand = brand
        self.message = message
    
    def power_on(self):
        """Turn on thermostat"""
        print("Powering on!")
        self.temp_set()
    
    def temp_set():
        """Input temperature"""
        bad_input = True
        
        while bad_input:
            try:
                temperature = input("Enter a valid temperature: ")
                temperature = int(temperature)
                bad_input = False
            except ValueError as ve:
                print(f"That is not a valid temperature, please try again!")
        print(f"You entered {temperature} Fahrenheit!")